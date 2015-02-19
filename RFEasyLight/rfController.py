import json
import socket

class RFController():
    SERVER_ADDR = "192.168.1.7"
    SERVER_PORT = 5337

    PROTOCOL = "nexa_switch"

    def __init__(self, config_file = "config"):
        self._load_config(config_file)

    #load from file later
    def _load_config(self, filename):
        with open(filename, "r") as config_file:
            self._config = json.load(config_file)

    def _get_code(self, device_name, attr, value = 1):
        _id = self._config[device_name]["id"]
        _unit = self._config[device_name]["unit"]
        return {"id": _id, "unit": _unit, attr: value}
        
    def turn_on(self, device_name):
        self._send(self._get_code(device_name, "on"))

    def turn_off(self, device_name):
        self._send(self._get_code(device_name, "off"))

    def dim_up(self, device_name):
        pass

    def dim_down(self, device_name):
        pass

    def all_on(self):
        pass

    def group_on(self, group_name):
        pass

    def group_off(self, group_name):
        pass
        
    def _init_conn(self, worker):
        init_data = {"message" : "client sender"}
        worker.write(json.dumps(init_data))
        worker.flush()
        
        result = worker.readline()
        print("init response %s"%(json.loads(result)))
        
        
    def _send(self, code):
        code["protocol"] = [self.PROTOCOL]
        send_data  = {"message": "send", "code": code}
        
        try:
            self._pilight_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._pilight_server.connect((self.SERVER_ADDR, self.SERVER_PORT))
            worker = self._pilight_server.makefile(mode="rw")
            
            self._init_conn(worker)
                        
            worker.write(json.dumps(send_data))
            worker.flush()
            result = worker.readline()

        except Exception as e:
            print(str(type(e)) + " : " + str(e))
        finally:
            self._pilight_server.close()
