from requests import  *
from login import Client
class Product(Client):
	def __init__(self):
		#明确继承自上一级
		#也可以不写默认继承
		Client.__init__(self)
	def data_template(self):
		self.data = {
			"module": "Products",
			"func": "savebill",
			"apikey": '',
			"token": '',
			"username": '',
			'product_no': 'test.01',  # 1 产品编号
			'productname': 'prd_test',  # 2 产品名称
			'productcategory': '吸头系列',  # 3 产品类别
			'productsheet': '	96支/盒',  # 4 规格型号
			'cf_4394': 'help_code1',  # 5 助记码
			'cf_4395': '1001.01',  # 6 旧物料编码
			'cf_4396': 'prod desc',  # 7 描述
			'cf_4397': '吸头系列',  # 8 物料分组
			'cf_4398': '自制',  # 9 物料属性
			'cf_4399': '',  # 10 配置生产
			'cf_4400': '单选',  # 11 特征件子项
			'cf_4401': '否',  # 12 套件
			'usageunit': '盒',  # 13 计量单位
			'discontinued': 0,  # 14 禁用,checkbox
			'cf_4402': '',  # 15 禁用原因
			'cf_4403': 1,  # 16 允许采购
			'cf_4404': 1,  # 17 允许销售
			'cf_4405': 1,  # 18 允许库存
			'cf_4406': 1,  # 19 允许生产
			'cf_4407': 0,  # 20 允许委外
			'cf_4408': 0,  # 21 允许资产
			'cf_4409': 0,  # 22 是否灭菌
			'cf_4410': '13%',  # 23 默认税率
			'cf_4411': '产成品',  # 24 存货类别
			'cf_4412': '标准税率',  # 25 税分类
			'cf_4413': 0.00,  # 26 结算成本价加减价比例(%)
			'procostprice': 27,  # 27 参考成本价(RMB)
			'cf_4414': 28,  # 28 毛重
			'cf_4415': 29,  # 29 净重
			'cf_4416': 30,  # 30 重量单位
			'cf_4417': 31,  # 31 长
			'cf_4418': 32,  # 32 宽
			'cf_4419': 33,  # 33 高
			'cf_4420': 34,  # 34 体积
			'cf_4421': '米',  # 35 尺寸单位
			'cf_4506': '已审核',  # 36 数据状态
			'cf_4507': '否',  # 37 禁用状态
			'cf_4508': '否',  # 38 已使用
			'cf_4509': '盒',  # 39 库存单位
			'cf_4510': '支',  # 40 辅助单位
			'cf_4511': '库存单位-->辅助单位',  # 41 换算方向
			'cf_4512': '',  # 42 仓库
			'cf_4513': '',  # 43 仓位
			'cf_4514': 0.00,  # 44 单箱标准数量
			'cf_4515': '是',  # 45 可锁库
			'cf_4516': '否',  # 46 启用周期盘点
			'cf_4517': '1',  # 47 盘点周期
			'cf_4518': '否',  # 48 必盘
			'cf_4519': '',  # 49 库存单位换算率分子
			'cf_4520': '',  # 50 库存单位换算率分母
			'cf_4521': '是',  # 51 启用批号管理
			'cf_4522': '01-成品批号',  # 52 批号编码规则
			'cf_4523': '否',  # 53 启用保质期管理
			'cf_4524': '',  # 54 批号附属信息
			'cf_4525': '',  # 55 保质期单位,数字
			'cf_4526': 0,  # 56 保质期,数字
			'cf_4527': 0,  # 57 在架保寿期
			'cf_4528': 0,  # 58 参考成本
			'cf_4529': '',  # 59 成本单位
			'cf_4530': '人民币',  # 60 币别
			'cf_4531': '否',  # 61 最小库存预警
			'cf_4532': '否',  # 62 安全库存预警
			'cf_4533': '否',  # 63 最大库存预警
			'cf_4534': '否',  # 64 再订货点预警
			'cf_4535': 0,  # 65 最小库存
			'qtyearly': 0,  # 66 安全库存
			'cf_4536': 0,  # 67 再订货点
			'cf_4537': 0,  # 68 经济订货批量
			'cf_4538': 0,  # 69 最大库存
			'cf_4539': '盒',  # 70 销售单位
			'cf_4540': '盒',  # 71 销售计价单位
			'cf_4541': 0,  # 72 起订量
			'cf_4542': '销售单位',  # 73 超发控制单位
			'cf_4543': 0,  # 74 超发上限(%)
			'cf_4544': 0,  # 75 超发下限(%)
			'cf_4545': 0,  # 76 代理销售减价比例(%)
			'cf_4546': '',  # 77 税收分类编码
			'cf_4547': 0,  # 78 享受税收优惠政策,checkbox
			'cf_4548': '',  # 79 税收优惠政策类型
			'cf_4549': '',  # 80 销售分组
			'cf_4550': 0,  # 81 ATP检查
			'cf_4551': 0,  # 82 允许退货
			'cf_4552': 0,  # 83 部件可退
			'cf_4553': 0,  # 84 不参与可发量统计
			'cf_4554': 0,  # 85 管理成本
			'cf_4555': 0,  # 86 允许发布到订货平台
			'cf_4556': 1,  # 87 启用售后服务
			'cf_4557': 1,  # 88 生成产品档案
			'cf_4558': 0,  # 89 是否保修
			'cf_4559': '',  # 90 保修期
			'cf_4560': '日',  # 91 保修期单位
			'cf_4561': 1,  # 92 来料检验
			'cf_4562': 0,  # 93 产品检验
			'cf_4563': 0,  # 94 产品首检
			'cf_4564': 0,  # 95 库存检验
			'cf_4565': 0,  # 96 退货检验
			'cf_4566': 0,  # 97 发货检验
			'cf_4567': 0,  # 98 其他检验
			'cf_4568': 0,  # 99 受托材料检验
			'cf_4569': 0,  # 100 生产退料检验
			'cf_4570': 0,  # 101 启用库存周期复检
			'cf_4571': 0,  # 102 复检周期(天)
			'cf_4572': 0,  # 103 启用库存周期复检提醒
			'cf_4573': 0,  # 104 提醒提前期(天)
			'cf_4574': '',  # 105 抽样方案
			'cf_4575': '',  # 106 质检方案
			'cf_4576': '',  # 107 质检组
			'cf_4577': '',  # 108 质检员
			'cf_4578': '盒',  # 109 采购单位
			'cf_4579': '盒',  # 110 采购计价单位
			'cf_4580': '苏州赛普生物科技有限公司',  # 111 采购组织
			'cf_4581': '',  # 112 采购员
			'cf_4582': '',  # 113 默认供应商
			'cf_4583': '',  # 114 费用项目
			'cf_4584': '标准采购申请',  # 115 采购类型
			'cf_4585': 0,  # 116 配额管理
			'cf_4586': '顺序优先',  # 117 配额方式
			'cf_4587': 0,  # 118 最小拆分数量
			'cf_4588': 0,  # 119 是否VMI业务
			'cf_4589': 0,  # 120 需要请购
			'cf_4590': 0,  # 121 货源控制
			'cf_4591': 0,  # 122 收货提前天数
			'cf_4592': 0,  # 123 收货上限比例%
			'cf_4593': 0,  # 124 收货下限比例%
			'cf_4594': 0,  # 125 收货延迟天数
			'cf_4595': '',  # 126 默认条码规则
			'cf_4596': 1,  # 127 最小包装数
			'cf_4597': 1,  # 128 重复打印数
			'cf_4598': 0,  # 129 启用条码管理，checkbox
			'cf_4599': '盒',  # 130 委外单位
			'cf_4600': '盒',  # 131 委外计价单位
			'cf_4601': '普通委外订单',  # 132 委外类型
			'cf_4602': 0,  # 133 代理采购加成比例%
			'cf_4603': '',  # 134 生产车间
			'cf_4604': '盒',  # 135 生产单位
			'cf_4605': 0,  # 136 入库超收比例%
			'cf_4606': 0,  # 137 入库欠收比例%
			'cf_4607': '汇报入库-普通生产',  # 138 生产类型
			'cf_4608': '',  # 139 组织间受托类型
			'cf_4609': 0,  # 140 生产线生产,logical
			'cf_4610': 0,  # 141 序列号携带到父项,logical
			'cf_4611': '主业务单位数量',  # 142 倒冲数量
			'cf_4612': '盒',  # 143 子项单位
			'cf_4613': 0,  # 144 消耗波动%
			'cf_4614': 0,  # 145 变动损耗率%
			'cf_4615': 0,  # 146 固定损耗%
			'cf_4616': 1,  # 147 可为主产品，logical
			'cf_4617': 0,  # 148 可为联副产品,logical
			'cf_4618': 0,  # 149 启用ECN,logical
			'cf_4619': '直接领料',  # 150 发料方式
			'cf_4620': '',  # 151 倒冲时机
			'cf_4621': '',  # 152 发料仓库
			'cf_4622': '',  # 153 发料仓位
			'cf_4623': '最小发料批量',  # 154 超发控制方式
			'cf_4624': '1',  # 155 最小发料批量
			'cf_4625': 0,  # 156 领料考虑最小发料批量,logical
			'cf_4626': 0,  # 157 是否关键件
			'cf_4627': 0,  # 158 是否齐套件
			'cf_4628': '',  # 159 默认工艺路线
			'cf_4629': '',  # 160 标准工时
			'cf_4630': 0,  # 161 标准人员准备工时
			'cf_4631': 0,  # 162 标准人员实作工时
			'cf_4632': 0,  # 163 标准机器准备工时
			'cf_4633': 0,  # 164 标准机器实作工时
			'cf_4634': '',  # 165 产品模型
			'cf_4635': '',  # 166 模型物料
			'cf_4636': 'MRP',  # 167 计划策略
			'cf_4637': 'MTS10(考虑库存)',  # 168 制造策略
			'cf_4638': 'LFL(批对批)',  # 169 订货策略
			'cf_4639': '',  # 170 计划区
			'cf_4640': 0,  # 171 固定提前期
			'cf_4641': 0,  # 172 变动提前期
			'cf_4642': 0,  # 173 检验提前期
			'cf_4643': 0,  # 174 累计提前期
			'cf_4644': '月',  # 175 订货间隔期单位
			'cf_4645': 0,  # 176 订货间隔期
			'cf_4646': 0,  # 177 最大订货量
			'cf_4647': 0,  # 178 最小订货量
			'cf_4648': 0,  # 179 最小包装量
			'cf_4649': 0,  # 180 固定/经济批量
			'cf_4650': 0,  # 181 变动提前期批量
			'cf_4651': 0,  # 182 日产量
			'cf_4652': 0,  # 183 拆分批量
			'cf_4653': 0,  # 184 批量拆分间隔天数
			'cf_4654': 0,  # 185 需求时界
			'cf_4655': 0,  # 186 计划时界
			'cf_4656': '',  # 187 计划组
			'cf_4657': '',  # 188 计划员
			'cf_4658': '',  # 189 计划标识
			'cf_4659': 0,  # 190 按批号匹配供需,logical
			'cf_4660': '弱预留',  # 191 预留类型
			'cf_4661': 0,  # 192 安全库存
			'cf_4662': '',  # 193 ATO预测冲销方案
			'cf_4663': '',  # 194 产品系列
			'cf_4664': 1,  # 195 冲销数量
			'cf_4665': 0,  # 196 允许提前天数
			'cf_4666': 0,  # 197 提前宽限期
			'cf_4667': 0,  # 198 预计入库允许部分提前
			'cf_4668': 0,  # 199 允许延后天数
			'cf_4669': 0,  # 200 延后宽限期
			'cf_4670': 0,  # 201 预计入库允许部分延后
			'cf_4671': '天',  # 202 时间单位
			'cf_4672': 0,  # 203 偏置时间
			'cf_4673': '',  # 204 供应来源
			'cf_4674': '',  # 205 时间紧迫系数
			'cf_4675': '',  # 206 数量负荷系数
			'cf_4676': '',  # 207 订单进度分组
			'cf_4773': '',  # 208 采购组
			'cf_4774': 0,  # 209 允许退料
		}
		return(self.data)
	def demo(self):
		self.save(self.data)

	def save(self,data):
		Client.save(self,data,url="/crmapi/crmoperation.php")
	def query(self,fieldvalue='test.01'):
		res = Client.query(self,module='Products',fieldname='product_no',fieldvalue=fieldvalue,url="/crmapi/crmoperation.php")
		return(res)
	def queryByNumber(self,fieldvalue='test.01'):
		res = self.query(fieldvalue=fieldvalue)
		return(res)
	def queryByName(self,fieldvalue='prd_test'):
		res = Client.query(self, module='Products', fieldname='productname', fieldvalue=fieldvalue,url="/crmapi/crmoperation.php")
		return (res)


if __name__ =='__main__':
	prd = Product()
	print(prd)
	data_demo = prd.data_template()
	prd.save(data=data_demo)
	prd.demo()
	data2 =  prd.query()
	print(data2)
	data3 = prd.queryByName()
	print(data3)

