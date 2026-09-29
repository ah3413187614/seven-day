# V0.2 叙事润色与证据系统

89／89 既有节点逐一改写；仍为 356 个选项，没有新增节点或结局候选。正文 120–166 字符（含标点与换行），自然段分布：{3: 3, 2: 86}。场景唯一编辑入口为 scripts/narrative.py；content.py 保留原路由和动作结构，其旧 scene 槽不再用于构建。

## 编辑规则与已落地内容

移除 build.py 的第三至七日通用补长段；不再用第四日统一揭密把所有路线拉平。正文通过空行分段，由 UI 渲染独立 p；昨日实际后果放在纸面外的回声区。角色第一次实际相遇才补角色身份，画像与转述不登记相遇。

王庭用印玺、军粮、账册与问责推进；圣堂用病历、誓词、同意与照护推进；龙境用接头、骨管、契约与幼龙风险推进；边境用锅、桥板、种子与撤离推进。没有给每章统一追加抒情结语。

选择按钮只显示行动，不再呈现“你需要接受：必死／关系崩塌／将进入某结局”。正文保留当下合理可知的危险；选择后才显示实际日落后果。NG+ 仅在第四日多一句声音与抬头动作，不显示规律、条件或攻略。

## 十种真相及授予来源

| ID | 片段 | 节点来源 | 行动来源 |
|---|---|---|---|
| truth_hero_identity | 艾德里安与被称作魔王的承压者是同一人。 | d4_c_guard, d4_h_ledger, d4_h_revolt, d5_w_oath, d6_h_revolt, d7_h_revolt | d4_h_revolt_3, d6_h_revolt_4 |
| truth_abyss_function | 深渊积存被抽离的痛苦，封印压住回流而非消灭敌人。 | d4_w_ledger, d5_h_ledger, d5_w_ledger | d3_w_ledger_3, d4_c_ledger_4, d4_h_revolt_2, d4_w_revolt_4 |
| truth_container_system | 容器是仍有意愿的活人；停止与交接需要替代承压。 | d3_h_oath, d4_c_oath, d4_h_ledger, d4_h_revolt, d5_w_oath, d6_h_revolt, d7_h_revolt | d4_h_oath_4, d4_h_revolt_3, d4_w_oath_2, d6_h_revolt_4 |
| truth_church_edit | 教会删去了姓名或撤回同意的记录。 | d3_h_ledger, d4_h_oath, d4_h_ledger | d4_h_revolt_3, d6_h_revolt_4 |
| truth_kingdom_succession | 王庭知情并持续为候选人与现任容器调拨资源。 | d4_c_oath, d4_c_ledger |  |
| truth_dragon_network | 龙骨与古渠构成支路，出口和风险必须现场核对。 | d4_w_ledger, d4_v_ledger, d5_w_ledger, d6_c_ledger | d4_w_ledger_3 |
| truth_demon_history | 魔族也有平民与受害记录，军方不等于全部族人。 | d3_h_revolt, d3_v_guard, d4_h_revolt, d4_h_guard, d4_w_revolt |  |
| truth_common_people_cost | 工程与战争的代价落在具体住户身上。 | d2_v, d3_c_oath, d3_c_ledger, d3_h_guard, d4_c_revolt, d4_h_guard, d4_w_revolt, d4_w_guard, d4_v_oath, d4_v_ledger, d4_v_revolt, d4_v_guard, d5_c_ledger, d5_w_ledger, d5_w_guard, d5_v_ledger, d6_h_ledger |  |
| truth_sword_nature | 黎明回应愿付生命的意志，不能证明善恶。 | d3_w_oath, d4_w_oath |  |
| truth_goddess_origin | 古代分配意志取得强制征用权限；神性仍未证实。 | d5_h_ledger, d6_h_oath, d6_h_ledger | d4_h_oath_3, d5_h_ledger_1 |

取得每条片段时保存 knowledgeLog 的 day、source、evidence。既视感不进入 truths。现有合法路线最多取得 7／10 项，没有任何路线自动读完世界百科。片段不是分数，也不在玩家页面显示未解锁清单。

## 实际权限变化

| 选项槽 | 完整条件 | 证据不足时的实际行动／身份 | 完整／受限路径次数 |
|---|---|---|---|
| d4_w_oath_1 | {"truthsAll": [], "flagsAll": ["took_holy_sword"], "flagsAny": []} | 接受同伴对承压器的否决权，先不用圣剑作保证。／d5_c_guard | 1／3 |
| d4_w_oath_4 | {"truthsAll": [], "flagsAll": ["took_holy_sword"], "flagsAny": []} | 用脱落鳞片试接阵列，记录仍缺少的剑身数据。／d5_w_ledger | 1／3 |
| d6_c_ledger_1 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network"], "flagsAll": [], "flagsAny": []} | 只启动已有签名的试验支路，留下全网待检记录。／d7_c_ledger | 1／30 |
| d6_h_oath_3 | {"truthsAll": ["truth_goddess_origin", "truth_church_edit"], "flagsAll": [], "flagsAny": []} | 封存这座圣堂的征用令，请证人核对总核心来源。／d7_h_revolt | 12／40 |
| d6_w_oath_2 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network"], "flagsAll": [], "flagsAny": []} | 请工程队先辨认备用管道，自己维持原有接口。／d7_w_ledger | 5／54 |
| d6_w_ledger_1 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network"], "flagsAll": ["lattice_validated"], "flagsAny": []} | 只启动已有签名的试验支路，留下全网待检记录。／d7_v_ledger | 22／64 |
| d7_c_ledger_1 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network"], "flagsAll": [], "flagsAny": []} | 按已核实的局部线路稳住出口，护送维修队撤离。／hero | 1／30 |
| d7_h_ledger_1 | {"truthsAll": ["truth_goddess_origin"], "flagsAll": [], "flagsAny": []} | 封住已经辨清的本地征用接口，把未知线路留给复核者。／guardian | 64／52 |
| d7_h_revolt_2 | {"truthsAll": ["truth_goddess_origin"], "flagsAll": [], "flagsAny": []} | 封住已经辨清的本地征用接口，把未知线路留给复核者。／guardian | 104／34 |
| d7_h_revolt_3 | {"truthsAll": ["truth_hero_identity", "truth_container_system", "truth_abyss_function"], "flagsAll": [], "flagsAny": ["personal_buffer", "opened_backup_channel", "shared_load", "lattice_validated", "surrendered_power"]} | 先续接止痛管，陪医师寻找他能够安全停止的时刻。／hero | 7／131 |
| d7_w_oath_3 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network"], "flagsAll": [], "flagsAny": []} | 按已核实的局部线路稳住出口，护送维修队撤离。／hero | 76／336 |
| d7_w_ledger_1 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network"], "flagsAll": [], "flagsAny": []} | 按已核实的局部线路稳住出口，护送维修队撤离。／hero | 5／198 |
| d7_w_ledger_2 | {"truthsAll": ["truth_goddess_origin"], "flagsAll": [], "flagsAny": []} | 封住已经辨清的本地征用接口，把未知线路留给复核者。／witness | 76／127 |
| d7_w_guard_1 | {"truthsAll": [], "flagsAll": [], "flagsAny": ["protected_egg", "warmed_egg", "raised_dragon", "shared_dragon_care", "rotating_watch", "befriended_dragon"], "relationsMin": {"Dragons": 2}} | 把孩子交给已有的共同照护人，先回营地照顾相识的住户。／ordinary | 32／193 |
| d7_v_oath_1 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network", "truth_common_people_cost"], "flagsAll": ["lattice_validated"], "flagsAny": ["shared_load", "protected_refusal", "called_volunteers", "open_lattice"]} | 签下本地共同守桥协议，从第一班夜岗开始。／guardian | 22／379 |
| d7_v_ledger_1 | {"truthsAll": ["truth_abyss_function", "truth_dragon_network", "truth_common_people_cost"], "flagsAll": ["lattice_validated", "shared_load"], "flagsAny": []} | 维持本地木闸和轮值，只接回已经确认的一段水路。／guardian | 22／623 |
| d7_v_guard_3 | {"truthsAll": [], "flagsAll": [], "flagsAny": [], "arcProgressAny": ["free_to_responsible", "selfish_to_selfless", "ash_to_restraint"]} | 与邻人排好三班守夜，先守住最靠近的堤口。／guardian | 183／436 |
| d7_w_oath_sword_2 | {"truthsAll": ["truth_goddess_origin"], "flagsAll": [], "flagsAny": []} | 封住已经辨清的本地征用接口，把未知线路留给复核者。／guardian | 6／21 |

次数统计是一种周目中的状态到达次数，不是玩家概率。每个条件槽两种模式都有真实路径。同一 Day 7 节点的双路线菜单对照见 evidence-report-v02.json 的 sameLocationContrasts；龙巢共同监护另需龙族信任与照护经历，外堤独立守望会核查已发生的弧光转向。d7_c_revolt_3 与 d7_h_oath_dissent_2 原全域停机无法在其七日路线内取得证据，现固定为局部封存／救助，未保留虚假的全域选项。

账房第六日通过龙骨支路实测图取得网络来源；圣堂第六日通过拆机铭牌与原始权限表取得曙母来源。它们只属于抵达现场的路线，不是新的全路线统一揭密。

完整神谕停机须有曙母来源；完整分流须有回流与网络证据；永久共同承压另须试验、预备网与居民代价认知。医生送别艾德里安还需可用缓冲，缺证时只止痛并继续撤离。无剑时第四日改用承压器或鳞片，不凭空持剑。

## 24 条弧光逐项校验

| ID／称号 | 早段证据 | 中段转向 | 后段确认 |
|---|---|---|---|
| coward_to_brave／曾经离开，后来折返的人 | 第2日 带家人从山路撤离，把工具留给村长。 | 第3日 送家人到哨站后折返桥头。 | 第6日 请守卫接纳孩子，自己回去守最后的路。；第7日 带最后一队伤者穿过山口，然后放下武器。 |
| selfish_to_selfless／从争取掌控到承担代价 | 第3日 接管运输线，用情报收入养活病人。 | 第6日 把候选者全送出门，留下自己值守。 | 第7日 站在外环承担第一轮黑潮，掩护所有值守者退后。 |
| faithful_to_heretic／背叛神谕的守誓者 | 第1日 去圣辉教会，核对预言中被抹去的人名。 | 第6日 拆除神谕强制回路，将信仰留给个人。 | 第7日 断开强制神谕，与两族共同维护余下的封印。 |
| hero_to_tyrant／曾敢前行，如今令人跪下 | 第1日 带着故乡的粮单，响应王都召集。 | 第6日 接受交换，先保证自己的同伴存活。 | 第7日 让卫队驱逐证人，以封印危机为由永不交权。 |
| merciful_to_cruel／曾经温柔的刽子手 | 第3日 用自己的军饷雇船，不让士兵进村。 | 第6日 接入未经批准的龙晶，强行提高功率。 | 第7日 独占核心，以恐惧维持一座不会反抗的城。 |
| cruel_to_redeemed／交出危险力量的人 | 第4日 用炉芯吸收黑潮试样，亲身查清代价。 | 第6日 向受害者交还控制权，接受被永久封禁。 | 第7日 接下医院的终身守护契约，拒绝军事征用。 |
| follower_to_leader／终于自己签名的领袖 | 第2日 签下征召誓书，换取故乡的粮车。 | 第6日 用军令强制接入，保证系统完整。 | 第7日 戴上王冠，将封印维护纳入公开国法。 |
| idealistic_to_pragmatic／学会计算代价的勇者 | 第2日 签下征召誓书，换取故乡的粮车。 | 第5日 拆分教皇职权，交给医师与地方教区。 | 第7日 先续接止痛管，陪医师寻找他能够安全停止的时刻。 |
| pragmatic_to_idealistic／算尽得失之后仍然相信的人 | 第2日 留下核对军粮账，暂缓出征。 | 第5日 接印，保留继任制度并增设志愿见证。 | 第6日 承认拒绝权，在公开见证下接过权杖。；第7日 接下权杖，把拒绝与退出写成不可删改的教律。 |
| human_supremacist_to_peacemaker／从军令走向共同守望 | 第3日 签征马令，亲自跟随粮队承担责问。 | 第5日 先撤空外环再关闭，接受中央失守风险。 | 第6日 请两族水手共同守船，让家人先过河。；第7日 接下医院的终身守护契约，拒绝军事征用。 |
| coward_to_martyr／逃过一次，留下到最后 | 第2日 带家人从山路撤离，把工具留给村长。 | 第6日 把最后的船位留给家人，转身去守闸。 | 第7日 留下守住山口，让同行者全部先走。 |
| hero_to_demon_king／从迎险到接替的人 | 第1日 带着故乡的粮单，响应王都召集。 | 第5日 请瑟文留下照料信徒，由你参加承压。 | 第6日 请求同伴带走黎明的故事，只把痛苦留给自己。 |
| believer_to_inquirer／向神明追问的人 | 第2日 签下征召誓书，换取故乡的粮车。 | 第6日 把忏悔与赔偿写入继任公约。 | 第7日 永久停用强制神谕核心，保存其计算档案。 |
| conqueror_to_keeper／从争取掌控到照料他人 | 第3日 接管运输线，用情报收入养活病人。 | 第6日 和他约定交接时刻，不再把同意视为永久。 | 第7日 将封印外门改成共同哨所，与龙族轮值。 |
| free_to_responsible／自愿留下的无主之人 | 第3日 烧掉征用单，让每户自行决定是否出马。 | 第6日 由自己承担它索要的份额，拒绝指定替身。 | 第7日 站在外环承担第一轮黑潮，掩护所有值守者退后。 |
| martyr_to_selfowner／终于把自己也算作一个人 | 第3日 送出自己的行粮，再押奥伦去教会作证。 | 第5日 准备终止分配意志，让各地自行承压。 | 第7日 拒绝任何职务，回村照料幸存的邻人。 |
| scholar_to_actor／从书页走入风暴的人 | 第3日 把王令交给修女，请她核查征用名单。 | 第5日 公开瓦尔扣押粮车的证据，逼其退让。 | 第7日 带最后一队伤者穿过山口，然后放下武器。 |
| soldier_to_healer／放下军令的照护者 | 第3日 签征马令，亲自跟随粮队承担责问。 | 第6日 和他约定交接时刻，不再把同意视为永久。 | 第7日 将封印外门改成共同哨所，与龙族轮值。 |
| healer_to_ruler／曾经照料别人，如今掌权的人 | 第3日 用自己的军饷雇船，不让士兵进村。 | 第6日 请求临时独裁到日落，用效率赌信任。 | 第7日 戴上王冠，将封印维护纳入公开国法。 |
| ruler_to_neighbor／放下掌控，另择道路的人 | 第3日 接管运输线，用情报收入养活病人。 | 第5日 烧掉强制候选名单，请信徒自行离开。 | 第7日 拒绝任何职务，回村照料幸存的邻人。 |
| skeptic_to_oathkeeper／质疑之后仍愿守约的人 | 第3日 把王令交给修女，请她核查征用名单。 | 第6日 亲自主持继任仪式，并写明退出权。 | 第7日 接下权杖，把拒绝与退出写成不可删改的教律。 |
| oathkeeper_to_free／把誓言还给人的守望者 | 第2日 签下征召誓书，换取故乡的粮车。 | 第5日 烧掉强制候选名单，请信徒自行离开。 | 第7日 拒绝任何职务，回村照料幸存的邻人。 |
| ash_to_restraint／让深渊止于自己的人 | 第3日 吞入炉芯灰烬，以自身替代燃料。 | 第6日 留下维持灯与呼吸机，让医师只管救治。 | 第7日 留在最后一盏灯下，以生命维持重症屏障。 |
| kindness_to_boundary／温柔终于有了边界 | 第3日 用自己的军饷雇船，不让士兵进村。 | 第4日 先登记所有空白村，再动工修渠。 | 第6日 将种子、病历和钥匙分别交给三个孩子。；第7日 维持本地木闸和轮值，只接回已经确认的一段水路。 |

上述是检测见证，最终显示称号仍可能被罪责或更高优先级特殊结局覆盖。完整选择 ID 与前后状态见 evidence-report-v02.json。军人弧光必须有民兵或征马经历；求权不自动等于当过国王，援助不自动等于医师；接触灰烬不自动判为残酷。恐惧强制供能、无辜者死亡、强征与背叛均保留罪责，收束不作自赦。

## NPC 与尾声

14 名角色每人补齐 protects、will_sacrifice、red_line、bias、mistake、secret、can_change、cannot_change。当前在场且已有相遇的关键角色可在回声区回应冲突；尾声只迭代 metNPCs。死亡古龙不再作为活体重遇，后续由遗誓使处理事务。角色值观表是写作约束，不声称每条都有独立事件树。

旧版 168 活跃称号逐项评级；其中 38 个正式题名改写，24 个重点尾声包完整重写。运行时按身份包＋本次终局行动＋实际相遇＋不可撤销伤害＋七日记录收束，不宣称 168 篇独立长文。

## 全节点段落清单

| 节点 | 标题 | 字符 | 段数 |
|---|---|---:|---:|
| d1_start | 第七声钟响之前 | 166 | 3 |
| d2_c | 粮单与冠冕 | 137 | 2 |
| d2_h | 钟楼下的删文 | 142 | 2 |
| d2_w | 没有守卫的剑 | 150 | 3 |
| d2_v | 桥只够过一辆车 | 158 | 3 |
| d3_c_oath | 印玺的背面 | 132 | 2 |
| d3_c_ledger | 账外的冬粮 | 129 | 2 |
| d3_c_revolt | 广场没有屋顶 | 128 | 2 |
| d3_c_guard | 车轮下面 | 138 | 2 |
| d3_h_oath | 誓词里的空位 | 152 | 2 |
| d3_h_ledger | 同一张病历 | 148 | 2 |
| d3_h_revolt | 证人的舌头 | 133 | 2 |
| d3_h_guard | 一床两伤 | 124 | 2 |
| d3_w_oath | 剑没有宣判 | 126 | 2 |
| d3_w_ledger | 地下的河 | 132 | 2 |
| d3_w_revolt | 被夺走的冬天 | 126 | 2 |
| d3_w_guard | 巢外的契约 | 125 | 2 |
| d3_v_oath | 长官的第一道命令 | 131 | 2 |
| d3_v_ledger | 名单最后一行 | 133 | 2 |
| d3_v_revolt | 山路朝着身后 | 124 | 2 |
| d3_v_guard | 留下的人 | 129 | 2 |
| d4_c_oath | 王令以下的真相 | 138 | 2 |
| d4_c_ledger | 并不存在的胜利 | 128 | 2 |
| d4_c_revolt | 胜利的口号 | 131 | 2 |
| d4_c_guard | 被救者的名字 | 152 | 2 |
| d4_h_oath | 神谕的呼吸 | 150 | 2 |
| d4_h_ledger | 七百年的同一个人 | 132 | 2 |
| d4_h_revolt | 魔王没有宝座 | 130 | 2 |
| d4_h_guard | 医院里的魔王画像 | 127 | 2 |
| d4_w_oath | 黎明承认的怪物 | 127 | 2 |
| d4_w_ledger | 龙骨是管道 | 132 | 2 |
| d4_w_revolt | 力量的饥饿 | 121 | 2 |
| d4_w_guard | 幼龙也会燃烧 | 125 | 2 |
| d4_v_oath | 没有被选中的人 | 135 | 2 |
| d4_v_ledger | 地图上的空白村 | 140 | 2 |
| d4_v_revolt | 安全领的关卡 | 128 | 2 |
| d4_v_guard | 家门里的旧王 | 129 | 2 |
| d5_c_oath | 王冠的抵押 | 133 | 2 |
| d5_c_ledger | 会算错的救命账 | 131 | 2 |
| d5_c_revolt | 革命也要钥匙 | 122 | 2 |
| d5_c_guard | 玛伦没有拔剑 | 124 | 2 |
| d5_h_oath | 祭坛前的空椅 | 128 | 2 |
| d5_h_ledger | 真相的使用说明 | 138 | 2 |
| d5_h_revolt | 停火的刀鞘 | 127 | 2 |
| d5_h_guard | 医院不能成为国家 | 123 | 2 |
| d5_w_oath | 容器的同意 | 138 | 2 |
| d5_w_ledger | 不能保证的第三条路 | 141 | 2 |
| d5_w_revolt | 下一次饥饿 | 133 | 2 |
| d5_w_guard | 一枚卵的重量 | 122 | 2 |
| d5_v_oath | 平民的议事桌 | 126 | 2 |
| d5_v_ledger | 最后一船工具 | 129 | 2 |
| d5_v_revolt | 自由的边界 | 128 | 2 |
| d5_v_guard | 门钥匙的去处 | 126 | 2 |
| d6_c_oath | 无人替你签字 | 126 | 2 |
| d6_c_ledger | 误差栏的签名 | 163 | 2 |
| d6_c_revolt | 胜利之前的审判 | 124 | 2 |
| d6_c_guard | 骑士的最后一班岗 | 131 | 2 |
| d6_h_oath | 没有赦罪的祝福 | 147 | 2 |
| d6_h_ledger | 曙母的第二个答案 | 127 | 2 |
| d6_h_revolt | 旧勇者请求睡眠 | 122 | 2 |
| d6_h_guard | 最后的病房灯 | 128 | 2 |
| d6_w_oath | 剑柄与扶手 | 125 | 2 |
| d6_w_ledger | 试验要有人签名 | 127 | 2 |
| d6_w_revolt | 深渊懂得你的名字 | 126 | 2 |
| d6_w_guard | 天亮前的看守人 | 126 | 2 |
| d6_v_oath | 没有英雄的会议 | 131 | 2 |
| d6_v_ledger | 渡船的第七次往返 | 120 | 2 |
| d6_v_revolt | 世界没有追上来 | 123 | 2 |
| d6_v_guard | 你不必成为传说 | 131 | 2 |
| d7_c_oath | 印玺的日落 | 130 | 2 |
| d7_c_ledger | 最后一笔预算 | 136 | 2 |
| d7_c_revolt | 刑台与议事桌 | 140 | 2 |
| d7_c_guard | 路的尽头还有人 | 127 | 2 |
| d7_h_oath | 祷词之后的回答 | 128 | 2 |
| d7_h_ledger | 不可删去的一页 | 130 | 2 |
| d7_h_revolt | 魔王最后的名字 | 128 | 2 |
| d7_h_guard | 病房门外的黎明 | 120 | 2 |
| d7_w_oath | 椅子不是王座 | 124 | 2 |
| d7_w_ledger | 图纸外的一毫米 | 125 | 2 |
| d7_w_revolt | 没有人能命令你 | 121 | 2 |
| d7_w_guard | 鳞片与炊烟 | 124 | 2 |
| d7_v_oath | 你的椅子也是木头 | 120 | 2 |
| d7_v_ledger | 让明天不再需要一个人 | 121 | 2 |
| d7_v_revolt | 门在你身后关上 | 130 | 2 |
| d7_v_guard | 第七碗汤 | 137 | 2 |
| d7_w_oath_sword | 黎明的四种用途 | 126 | 2 |
| d7_w_guard_dragon_debt | 没有古龙签名的契约 | 124 | 2 |
| d7_c_oath_judgment | 加冕之前，先读出名单 | 121 | 2 |
| d7_h_oath_dissent | 曾经离开的人回来了 | 131 | 2 |