#说明

扫描全网的ES，并列举每个索引、每个类型中的十条记录，以判断此ES是否遭受过攻击

config.py中，修改source_list指向要检查的ES服务器地址

	$python scan.py |tee result.txt

没有对结果做任何筛选，请手工进行判断