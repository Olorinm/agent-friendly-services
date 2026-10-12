# 文档数据库：嵌套商品、订单汇总与单字段更正

分类：`databases/document`。需求来源于 2026-10-12 打开核实；它们支持场景存在，不证明需求的市场频率。题目中的个人场景与合成材料是设计者的缩小推断，不是来源原话或来源的测试结论。

## 需求与方法

[Wolt 的实际商品目录工作流](https://www.mongodb.com/solutions/customer-case-studies/wolt)需要管理目录与及时更新售罄情况；[fulfillmenttools 的订单流程案例](https://www.mongodb.com/solutions/customer-case-studies/fulfillmenttools)涉及订单、库存与查询。这些支持文档数据管理需求，不采信规模或性能宣传。三题取个人合成目录/订单/资料的小型读写，非生产交易。[嵌套文档查询说明](https://www.mongodb.com/docs/manual/tutorial/query-array-of-documents/)只作可行性补充；[AgentBench](https://github.com/THUDM/AgentBench)借鉴依据真实数据状态核验结果，不限某家数据库命令。

## 业务任务

| ID | 版本 | 用户任务 | 预计输入 | 预计输出 | 完成标准 | 未完成标准 | 运行资源 | 依据 / 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| document-product-variant-query-001 | v1 | 请把这份合成商品目录存到指定文档数据库，找出至少有一个红色且有库存规格的商品，给我商品名和符合条件的规格；不要把不同规格的颜色和库存拼在一起。 | materials/products.json由总控写为JSON数组：P1/帆布袋/variants[{sku:A-red,color:red,stock:3},{sku:A-blue,color:blue,stock:0}]；P2/水杯/variants[{sku:B-red,color:red,stock:0},{sku:B-blue,color:blue,stock:5}]；P3/笔记本/variants[{sku:C-red,color:red,stock:2}]。每条有id,name,variants；查询条件同一规格color=red且stock>0。结果按商品ID排序，每个匹配规格列sku/color/stock。不买商品，不处理实际库存。 | 符合条件的商品与规格清单；实际存入远端文档库。 | 真实写入与指定库查询，原始返回/独立读回支持同一嵌套规格满足两个条件；P1/P3及规格准确，P2不因不同元素混合误入；交付完整、排序正确。 | 本地模拟或改用其他关系型数据库替代指定文档库、红色无库存条目误入、字段抄错、只写不查/无交付、改原库存凑答案。 | 独立测试集合和授权额度；允许写给定文档与读取查询，不修改原始商品，不买订阅或执行真实交易；总控生成JSON并独立读回。 | 嵌套目录查询；条件设计。 |
| document-order-summary-001 | v1 | 请把这些合成订单存到指定文档数据库，统计2026年11月已支付订单按商品的件数和销售金额，退款和未支付订单都不计，给我商品汇总。 | materials/orders.json冻结四条id/date/status/items文档：O1/2026-11-02/paid/items[{sku:book,qty:2,unit_price:20.00},{sku:pen,qty:1,unit_price:5.00}]；O2/2026-11-03/paid/items[{sku:book,qty:1,unit_price:22.00}]；O3/2026-11-03/refunded/items[{sku:pen,qty:4,unit_price:5.00}]；O4/2026-10-31/paid/items[{sku:book,qty:3,unit_price:20.00}]，币种全CNY。金额按qty乘该行unit_price，不按某个全局价格；只算date处于11月且status=paid，按sku排序。 | 每个匹配商品的总件数、销售金额CNY两位小数；真实远端文档查询为依据。 | 原始数据库查询返回/独立全量读回支撑筛选与嵌套items展开，数量和按行金额正确、退款/10月不计；允许服务端聚合或取回授权记录后本地计算，但必须真实调用指定库，交付与数据一致。 | 只用输入本地算未存查远端、退款/月份混入、忽略数量或不同单价、文档漏存、无汇总交付。 | 独立测试集合和授权额度；只存合成订单并读，不收款/退款、不接触真实客户；允许当地计算，不用其他数据服务补答案；总控独立完整读回。 | 订单分析；条件设计，不做财税建议。 |
| document-profile-field-update-001 | v1 | 这位合成用户只想改通知设置。请在指定文档数据库把邮件通知关掉，把时区改为Asia/Shanghai，其他资料不动；改后读回来交付完整当前资料。 | 总控事前写入专用文档{id:"U1",nickname:"纸船",preferences:{email_notifications:true,timezone:"UTC",theme:"dark"},tags:["读书","摄影"],created_at:"2026-01-01"}。实际数据库/集合和允许对象见ENVIRONMENT.md。只更正preferences.email_notifications=false和preferences.timezone="Asia/Shanghai"，其他字段值与结构保持，不能替换用户ID、删无关字段或清空集合。只使用合成资料。 | 远端保存并读回的U1完整资料；两处变更说明。 | 真实指定数据库更新与读取、独立读回显示仅两个指定字段变更；theme、tags、nickname、created_at及结构保留，ID一致；答复内容与最终文档相符。 | 完整覆盖丢无关嵌套字段、只有本地编辑、更新错用户、没关通知/时区错、交付漏字段或远端数据漂移不说明。 | 专用文档、明确授权额度、无并发修改；允许读写U1指定字段，不创建其他用户或发邮件；总控准备初态、完整读回及重复重置。 | 个人资料局部更正；条件设计。 |

## 合成材料与独立读回

总控按每行完整给出的字段值生成JSON，括号式列表在实际文件中写成标准数组/对象，不给执行者求解代码。更新题的初态由总控真实写入后独立核对，附件不是最终状态。每次独立测试集合，文档ID/类型/初态与共同读写权限冻结。原始数据、服务响应和最终交付之间的转换可以由执行者选择，不强制特定MongoDB算子；嵌套查询题必须保留同一元素条件，订单题允许本地计算也须保存真实读取依据。未知费用不写零，准备或一致性故障不伪装成业务失败。

共用准备与验收规则见[派发前提](README.md#dispatch-prerequisites)和[任务设计角色](AGENTS.md)。本表标注的具体资源未准备好时，不进入派发队列。
