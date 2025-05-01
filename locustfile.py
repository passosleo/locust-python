from locust import HttpUser, task, between

class W3SchoolsUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://www.w3schools.com"

    @task(4)
    def home_page(self):
        self.client.get("/")

    @task(3)
    def learn_html(self):
        self.client.get("/html/")

    @task(3)
    def learn_css(self):
        self.client.get("/css/")

    @task(2)
    def learn_javascript(self):
        self.client.get("/js/")

    @task(1)
    def try_it_editor(self):
        # Simula acesso ao editor de código "Try it Yourself"
        self.client.get("/tryit/trycompiler.asp?filename=demo_python")

    @task(1)
    def use_color_picker(self):
        # Simula o uso da ferramenta de seleção de cores
        self.client.get("/colors/colors_picker.asp")

    @task(1)
    def play_codegame(self):
        # Simula acesso ao CodeGame interativo
        self.client.get("/codegame/index.html")
