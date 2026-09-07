<!-- GENERATED FILE — do not edit. -->
# 用户需求与场景研究

本页展示研究档案，不代表正式测试集或市场频率统计。reported 是公开用户表达，inferred 是资料推断，hypothesis 是待找证据的想法。来源组计数仅辅助去重。

[维护说明](../docs/contributing.md#research-user-needs) · [完整数据](./research.json)

## travel/flights

[机票用户需求与场景研究（首轮公开资料）](../data/research/travel/flights.yaml)

理解普通个人使用机票相关服务的真实情境、期望结果、约束与分歧；持续寻找常见需求的证据，不把公开帖子数量当作市场频率。

来源 25；公开表达 13；推断 1；假设 0。

| 需求 | 用户与触发情境 | 希望得到的结果 | 依据类型 | 来源 |
| --- | --- | --- | --- | --- |
| choose-fixed-trip | 地点和出行日已确定的个人：需要在可接受的起降时段内选票，避免为了便宜牺牲安排。 | 比较满足日期和时段的可购买方案，理解当地起降日期、时间与价差。 | reported | [v2-fixed-price](https://v2ex.com/t/1047113), [tse-timezone](https://travel.stackexchange.com/questions/102386/does-the-flight-time-when-booking-a-holiday-online-show-the-time-you-arrive-in-t) |
| compare-family-total | 替家庭或多人同行购票的人：低票价可能不满足孩子与家长同坐或多人靠近的需要，选座成本较晚才清楚。 | 得到符合具体同行关系、预算和座位要求的全部旅客费用及可安排程度。 | reported | [reddit-family-price](https://www.reddit.com/r/TravelHacks/comments/1pwz8bd/flight_price_transparency/), [tse-child-adult](https://travel.stackexchange.com/questions/94078/do-gate-agents-really-seat-young-children-away-from-their-parents-in-united-basi), [tse-family-seven](https://travel.stackexchange.com/questions/132292/how-to-seat-family-of-seven-together-on-long-haul-flight) |
| explore-flexible-trip | 目的地或区域有方向，但机场和日期有弹性的个人：逐个尝试往返日期和机场费时，某些条件不能同时生效。 | 在允许的日期与机场组合中找到可接受的行程，并比较时间、总费用和购买途径。 | reported | [tse-flex-airports](https://travel.stackexchange.com/questions/174551/finding-a-flight-with-flexible-date-and-flexible-airports), [tse-allin-flex](https://travel.stackexchange.com/questions/182569/flight-search-by-total-cost-including-auxiliary-fees), [v2-international-bags](https://v2ex.com/t/921145) |
| compare-total-cost | 需要携带行李或使用付费附加项目的旅客：搜索最低价无法直接反映个人所需的完整费用，付款后才发现选错。 | 按相同旅客需求比较含税费及所需附加项目的总价，并列出未知费用。 | reported | [tse-bag-total](https://travel.stackexchange.com/questions/9921/are-there-any-flight-price-search-engines-with-baggage-allowance-included), [tse-allin-flex](https://travel.stackexchange.com/questions/182569/flight-search-by-total-cost-including-auxiliary-fees), [reddit-family-price](https://www.reddit.com/r/TravelHacks/comments/1pwz8bd/flight_price_transparency/), [v2-international-bags](https://v2ex.com/t/921145), [v2-fixed-price](https://v2ex.com/t/1047113) |
| explore-open-destination | 想利用周末出游、尚未选定目的地的个人：愿意依据机票价格选地方，但工作时间限制了可出发和返回时段。 | 在可用时间内比较目的地，找到值得去且能够按时回来的选择。 | reported | [tse-weekend-anywhere](https://travel.stackexchange.com/questions/42721/searching-for-flights-to-anywhere-in-narrow-time-frame) |
| plan-multicity | 想在一次出行中游览多个城市的个人：普通往返搜索能找到价格，但增加中途停留后必须反复手动试日期。 | 比较满足城市顺序和停留目的的整段方案与总费用。 | reported | [tse-multicity](https://travel.stackexchange.com/questions/108093/how-to-search-for-a-multi-destination-flight-when-flexible-on-dates) |
| check-connection | 考虑或已经购买中转航班的个人：无法判断便宜组合属于何种衔接、是否需过境手续或重新处理行李。 | 明确衔接方式、待办手续和未知条件，判断方案是否适合自己的证件和时间限制。 | reported | [tse-no-selftransfer](https://travel.stackexchange.com/questions/191493/flight-search-engine-that-can-show-the-cheapest-flight-excluding-self-transfer-a/191495), [tse-transit-visa](https://travel.stackexchange.com/questions/183766/indian-passport-holder-with-a-self-transfer-in-abu-dhabi), [qyer-transfer-security](https://ask.qyer.com/question/4253406.html) |
| choose-booking-channel | 在航司直购与第三方渠道间作选择的个人：相同或类似行程价格不同，担心售后，也可能遇到航司网站支付障碍。 | 比较可用渠道的实际价格、支付可用性和后续处理路径，按本人的偏好决定。 | reported | [reddit-ota-tradeoff](https://www.reddit.com/r/Flights/comments/1mr4x7l/are_ota_worth_it_sometimes/), [v2-international-bags](https://v2ex.com/t/921145), [v2-fixed-price](https://v2ex.com/t/1047113), [iata-gps-2025](https://www.iata.org/en/pressroom/2025-releases/2025-11-05-02/) |
| confirm-purchasable | 找到报价准备买票、或已经提交预订的个人：低价缺少能继续购买的入口，或预订后无法确认何时出票。 | 知道选中方案能从哪里买、当前费用是否成立，以及已预订的订单到底处于什么状态。 | reported | [tse-unbookable-price](https://travel.stackexchange.com/questions/148416/book-with-a-travel-agent-option-on-google-flights), [tse-flex-airports](https://travel.stackexchange.com/questions/174551/finding-a-flight-with-flexible-date-and-flexible-airports), [v2-ticketing-delay](https://www.v2ex.com/t/281472), [v2-fixed-price](https://v2ex.com/t/1047113) |
| watch-price | 出行已知但尚未决定何时付款的个人：票价会变化，既想等低价，又怕卖完；历史信息和连续查看费时。 | 获得观察期间的价格变化与可购买性信息，帮助决定何时出手。 | reported | [v2-fixed-price](https://v2ex.com/t/1047113) |
| change-or-refund | 购票后计划发生变化的个人或家庭：希望取消或调整行程，但不同票段的损失与处理方式不清楚。 | 按当前订单弄清可选操作、退款或补差成本和下一步处理路径。 | reported | [v2-family-refund](https://www.v2ex.com/t/1044166), [v2-fixed-price](https://v2ex.com/t/1047113) |
| recover-disruption | 收到航班变更通知或行程受影响的旅客：担心出行中断，匆忙另购可能与原订单状态冲突并产生额外费用。 | 了解当前有效状态，找到继续出行或结束订单的选项及处理顺序。 | reported | [v2-cancel-resume](https://v2ex.com/t/1057821), [reddit-ota-tradeoff](https://www.reddit.com/r/Flights/comments/1mr4x7l/are_ota_worth_it_sometimes/) |
| arrange-assistance | 替独自出行且需要协助的家人安排旅程的人：仅知道航班价格，无法确认机场及转机途中有人提供需要的帮助。 | 在选机场和行程时确认协助范围、预约路径、费用及尚需人工确认的部分。 | reported | [tse-senior-assistance](https://travel.stackexchange.com/questions/193909/do-special-assistants-wait-at-the-gate-with-senior-passengers-im-worried-my-78), [tse-airport-assistance](https://travel.stackexchange.com/questions/3354/what-options-are-there-for-disabled-assistance-at-heathrow-airport-or-which) |
| verify-notice | 收到声称航班取消或可退款消息的个人：消息掌握行程信息仍可能不可信，用户担心身份和旅行信息的使用。 | 通过可核验的航班/订单和联系入口检查消息内容，辨别需要进一步确认的行动。 | inferred | [v2-fake-notice](https://www.v2ex.com/t/1119316), [v2-cancel-resume](https://v2ex.com/t/1057821) |

| 场景 | 关联需求 | 所需基础能力 | 研究状态 | 测试可行性 | 原因 |
| --- | --- | --- | --- | --- | --- |
| 固定行程下按时段与价格选票 | choose-fixed-trip | 按行程条件获取机票方案及报价。 | retained | feasible | 首轮先检查能否按日期、时段和人数找到航班；原帖支持这些约束，适合作为基础场景。 |
| 在日期与机场范围内比较完整费用 | explore-flexible-trip, compare-total-cost | 按行程条件获取机票方案及报价。<br>获取指定旅客和报价的行李额度、可加购项目及费用。<br>核验选中行程及已选项目的当前可售性与总费用。 | retained | unknown | 在基础选票之上增加日期与机场组合、行李费用比较；以真实需求约束扩展任务，跨帖合成已明确标注。 |
| 按家庭的座位关系比较总费用 | compare-family-total, compare-total-cost, confirm-purchasable | 按行程条件获取机票方案及报价。<br>获取指定报价的座位选项、费用与安排条件。<br>核验选中行程及已选项目的当前可售性与总费用。<br>提供选中方案可继续购买的入口和关联条件。 | retained | unknown | 在选票与费用比较之外，进一步检查座位关系、安排确定性及购买衔接；原帖中的不同付费意愿分别保留。 |
| 目的地不限的周末出游 | explore-open-destination, choose-fixed-trip | 待拆解 | retained | unknown | 目的地开放与日期开放有不同的验收条件，单独保留。 |
| 有游览停留目的的多城市行程 | plan-multicity, check-connection | 待拆解 | retained | unknown | 多段搜索服务于中途游览目标；具体能否统一出票及成本仍待测试。 |
| 确认中转组合是否适合本人 | check-connection | 待拆解 | retained | unknown | 原帖支持证件与转机方式的困惑；场景应容许有依据地报告无法确认。 |
| 选定航班后的渠道与购买衔接 | choose-booking-channel, confirm-purchasable | 待拆解 | retained | unknown | 渠道选择要保留价差与便利性的不同偏好，不能预设直购或 OTA 获胜。 |
| 已定出行的观察票价与买票决策 | watch-price, choose-fixed-trip | 待拆解 | retained | unknown | 保留购买时机这一跨时间目标，无法在一次调用中完成也不删除。 |
| 计划变化后比较退改选择 | change-or-refund | 待拆解 | retained | unknown | 售后需求不能从单纯搜索测试的范围反推为不重要。 |
| 航班状态变化后安排下一步 | recover-disruption, change-or-refund | 待拆解 | retained | unknown | 取消又恢复的例子说明状态一致性会改变操作顺序；保持原订单与新选择的联系。 |
| 把所需协助纳入机场和航班选择 | arrange-assistance, check-connection | 待拆解 | retained | unknown | 服务边界影响能否完成旅程，保留在机票相关需求内；可能涉及相邻服务。 |
| 核验声称取消航班的消息 | verify-notice | 待拆解 | candidate | unknown | 保留为候选，待补查用户委托意愿和服务边界。 |

待研究与覆盖缺口：

- 这是2026-09-07进行的目的性、迭代式公开资料采样：21条实际查询，22个用户原帖组（其中1个仅索引正文），另有1项调查的2个页面和沿用的1份产品文档。不是随机样本，未达到或声称主题饱和。
- 用户材料来自 Travel Stack Exchange、V2EX、Reddit、穷游问答；中文和英文，偏可被搜索引擎检索的提问者、技术社区与困难案例。成功且无困扰的购买、普通低频旅客可能被低估，登录社区未充分覆盖。
- 旧帖证明当时出现过需求，不证明当前仍有同样产品缺陷；有明确发帖日期的材料从2011年至2025年，仍缺2026年的新增原始诉求及稳定复查机制。checked_on只表示本轮阅读日期，不是产品测试日期或页面最新版本保证。
- 13项 reported 指需求有直接表达支持，1项 inferred 是研究者推导；12个场景均为研究者改写/合成。11项 retained 表示本轮保留，1项 candidate 待补查；研究结束时全部测试可行性未知。随后仅fixed-itinerary完成本地探索试跑并更新为feasible，其余场景仍待验证；研究场景保留不等于任务通过。
- IATA总体偏好调查不能推出我们的任务频率。样本内复现、市场发生频率、未满足程度、失败后损失应分别讨论；本轮没有足够证据给场景排市场高频榜或设覆盖率权重。
- 后续优先补：普通顺利购买、时间优先与紧急出行、国内外不同市场、支付/出票失败、婴儿/未成年人、无障碍旅客本人、多人异地会合、里程与现金、商务舱/舒适度、航班延误后的实际改路。
- 机场接驳、机酒预算、到达日与酒店日期、租车、保险、宠物及环保偏好等相邻或未覆盖需求不可据本轮资料直接排除。知识缺口与供应商能力缺口分开记录。
- v2-ticketing-delay只能从检索索引读到原帖短正文，后续需原页复查或新增一手材料；r/Flights机器人警告、合并问答、同帖回复与镜像不增加独立用户样本数。未核验论坛身份或所有潜在转载关系。
- 能力候选有些尚包含多个动作，需要技术资料校准并根据实际测试继续拆分；输出字段、用户约束、Agent推理和服务动作不机械一一对应。仅search-offers和purchase-handoff沿用已有词典映射。
- 下一步测试设计先说明用户、输入、结束状态、验收证据与比较口径，再查各服务入口和个人接入准备；不同入口不必重复算成独立服务，未接入不等于任务失败。研究范围不能为了第一轮能跑而缩成已支持功能。
