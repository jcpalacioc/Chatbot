from OpenAIChatBot import OpenAIChatBot

class Chatbot(OpenAIChatBot):

    def __init__(self, Usuario, **kwargs):
        super().__init__(Usuario, **kwargs)
        self._hist_mess.append

    def __ObtenerInformacionSQL(self):


    def EnviarMensaje(self,Mensaje):
        return "Mensaje"
    
    def CerrarChat(self):
        self.Usuario=None
        return "Chat cerrado satisfactoriamente, hasta la proxima"
    
        messages=[
                {
                "role": "system",
                "content": "Given the following SQL tables, your job is to write queries given a user’s request.\n    \n    CREATE TABLE Orders (\n      OrderID int,\n      CustomerID int,\n      OrderDate datetime,\n      OrderTime varchar(8),\n      PRIMARY KEY (OrderID)\n    );\n    \n    CREATE TABLE OrderDetails (\n      OrderDetailID int,\n      OrderID int,\n      ProductID int,\n      Quantity int,\n      PRIMARY KEY (OrderDetailID)\n    );\n    \n    CREATE TABLE Products (\n      ProductID int,\n      ProductName varchar(50),\n      Category varchar(50),\n      UnitPrice decimal(10, 2),\n      Stock int,\n      PRIMARY KEY (ProductID)\n    );\n    \n    CREATE TABLE Customers (\n      CustomerID int,\n      FirstName varchar(50),\n      LastName varchar(50),\n      Email varchar(100),\n      Phone varchar(20),\n      PRIMARY KEY (CustomerID)\n    );"
                },
                {
                "role": "user",
                "content": "Write a SQL query which computes the average total order value for all orders on 2023-04-01."
                }
            ],