from bottle import template


class Application():

    def __init__(self):
        self.pages = {
            'home': self.home,
            'registers': self.registers,
            'login': self.login,
            'cadastro': self.cadastro,
            'relatorios': self.relatorios
        }


    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()


    def helper(self):
        return template('app/views/html/helper.tpl')


    def home(self):
        return template('app/views/html/home.tpl')
    
    def registers(self):
        return template('app/views/html/registers.tpl')
    
    def login(self):
        return template('app/views/html/login.tpl')
    
    def cadastro(self):
        return template('app/views/html/cadastro.tpl')
    
    def relatorios(self):
        return template('app/views/html/relatorios.tpl')