"""Supported model routes; credentials stay in the controller-only proxy."""

DEFAULT_PROVIDER = 'zhipuai-coding-plan'
PROVIDERS = {
    DEFAULT_PROVIDER: {
        'id': 'zhipuai-coding-plan', 'name': 'BigModel Coding Plan',
        'host': 'open.bigmodel.cn', 'base_path': '/api/coding/paas/v4',
    },
    'deepseek': {
        'id': 'afs-deepseek', 'name': 'DeepSeek direct API',
        'host': 'api.deepseek.com', 'base_path': '/v1',
    },
}


def profile(name=DEFAULT_PROVIDER):
    if not isinstance(name, str) or name not in PROVIDERS:
        raise ValueError('Unsupported model provider')
    return PROVIDERS[name]


def validate_model(name, model):
    profile(name)
    valid = (model in ('deepseek-flash', 'deepseek-v4-pro') if name == 'deepseek'
             else isinstance(model, str) and model.startswith('glm-'))
    if not valid:
        raise ValueError('Model does not match the configured provider')


def opencode_config(request, name):
    validate_model(name, request['model'])
    route = profile(name)
    model_id = route['id'] + '/' + request['model']
    model = {'variants': {request['reasoning_effort']: {'reasoningEffort': request['reasoning_effort']}}}
    provider = {'options': {'apiKey': 'local-capture-proxy',
                           'baseURL': 'http://127.0.0.1:18181' + route['base_path']},
                'models': {request['model']: model}}
    if name == 'deepseek':
        provider.update(npm='@ai-sdk/openai-compatible', name=route['name'])
        model.update(name=request['model'], reasoning=True,
                     interleaved={'field': 'reasoning_content'},
                     limit={'context': 1048576, 'output': 32000})
    return {'$schema': 'https://opencode.ai/config.json', 'model': model_id, 'small_model': model_id,
            'share': 'disabled', 'autoupdate': False,
            'agent': {'title': {'disable': True}, 'summary': {'disable': True}},
            'permission': {'*': 'allow', 'task': 'deny', 'question': 'deny'},
            'provider': {route['id']: provider}}
