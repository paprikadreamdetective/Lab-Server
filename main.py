from factory.socketf import SocketFactory
from persistence.crudmongodb import crudMongoDB
import json
import uuid

# from persistence.crudCassandra import crudCassandra

# Hola mundo
def main():
    path_jsons ='/home/server/Documentos/CASSANDRA 4/Octa_json'
    multicast_socket_receiver = SocketFactory.create_multicast_socket('224.10.10.10', 10000)
    #db = crudCassandra('localhost', 9042)
    cnt = 0
    name_file = 'bd_'
    unique_id = uuid.uuid4()
    while True:
        print('Waiting to Receive Message')
        data, address = multicast_socket_receiver.receive_msg()
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)
        data_dict['ID_Experiment'] = str(unique_id)    
        with open(path_jsons + '/' + name_file + str(cnt) + '.json', 'w', encoding='utf-8') as archivo:
            json.dump(data_dict, archivo, ensure_ascii=False, indent=4)
        
        #print('Received {} bytes from {}'.format(len(data), address))
        print(data_dict)
        cnt += 1
        #db.create_experiment()
if __name__ == '__main__':
    main()



