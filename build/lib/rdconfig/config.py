'''
 * one class with 4 method
 * config file in 4 file format
 * which is ini,json,toml,yaml.
 * copyright: hulilei and reshape data service.
'''
from configparser import ConfigParser
import urllib.request
import json
import toml
import yaml
'''
 * Config is a config class object
 * author:hulilei
 * create date:2022-03-29
'''
class Config:
    def __init__(self,file_name):
        self.file_name = file_name
    def __str__(self):
        return (self.file_name)
    def read_ini(self,node_name='mysql'):
        self.node_name = node_name
        cfg_paser = ConfigParser()
        cfg_paser.read(self.file_name)
        res = dict(cfg_paser.items(self.node_name))
        return(res)
    def read_json(self,node_name='mysql'):
        self.node_name = node_name
        with open(self.file_name) as f:
            res = json.load(f)[self.node_name]
        return(res)
    def read_jsonUrl(self,node_name='mysql'):
        self.node_name = node_name
        with urllib.request.urlopen(self.file_name) as url:
            data = json.loads(url.read().decode())
        return(data[self.node_name])

    def read_toml(self):
        res = toml.load(self.file_name)
        return(res)
    def read_yaml(self):
        with open(self.file_name, 'r') as f:
            res = yaml.safe_load(f)
        return(res)

if __name__ == '__main__':
    cfg = Config(file_name='db.ini')
    bbc = cfg.read_ini(node_name='mysql')
    print(bbc)
    cfg_j = Config(file_name='db.json')
    bbj = cfg_j.read_json(node_name='mysql')
    print(bbj)
    cfg_t = Config(file_name='db.toml')
    bbt = cfg_t.read_toml()
    print(bbt)
    cfg_y = Config(file_name='db.yaml')
    bby = cfg_y.read_yaml()
    print(bby)

