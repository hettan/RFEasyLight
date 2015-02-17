import json
import urllib2

class RFController():
    SERVER_ADDR = "0.0.0.0"
    SERVER_PORT = "5000"

    PROTOCOL = "nexa_switch"

    def RFController(self, conf_file = None):
        #data = json.loads(conf_file)
        self._load_config(config)
        
        self._pilight_server(socket.AF_INET, socket.SOCK_STREAM)

    def _load_config(self, config):
        pass

    def turn_on(self, device_name):
        pass

    def turn_off(self, device_name):
        pass

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

    def _send(self, code):
        try:
            self._pilight_server.connect((SERVER_ADDR, SERVER_PORT))
            
            data  = {"message": "send",
                     "protocol": [PROTOCOL],
                     "code": code}
            
            worker = self._pilight_server.makefile(mode="rw")
        
            worker.write(json.dumps(data))
            worker.flush()
            result = worker.readline()

            print("response %s"%(data))
        except Exception as e:
            print(str(type(e)) + " : " + str(e))
        finally:
            self._pilight_server.close()
