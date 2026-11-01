import json

def load_config(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        return {"host": "localhost", "port": 8080, "debug": True}

def save_config(config,filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False,indent=2)

def show_config(config):
    for key,value in config.items():
        print(f"{key}:{value}")

def update_config(config):
    key = input("请输入要修改的配置项")
    if key in config:
        new_value = input("请输入新的值：")
        config[key]= new_value
    else:
        print("没有这个配置项")
    return config

def main():
    config = load_config("config.json")
    filename = "config.json"
    while True:
        print("1、查看配置:\n")
        print("2、修改配置:\n")
        print("3、保存并退出:\n")
        choice = input("请选择输入项：")
        if choice == "1":
            show_config(config)
        elif choice == "2":
            config = update_config(config)
            save_config(config,filename)
        elif choice == "3":
            save_config(config,filename)
            print("已保存，退出")
            break
        else:
            print("输入有误，请重重新选择")
# main()
# filename={
#     "host":"localhost",
#     "port":8080,
#     "debug":true
# }

