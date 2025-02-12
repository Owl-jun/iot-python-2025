class OuterClass:
    def __init__(self):
        self.outer_variable = "This is from the outer class"
        self.inner_instance = self.InnerClass(self,OuterClass)  # 이너 클래스의 인스턴스를 외부 클래스에서 생성

    def show_inner(self):
        print("Inside outer class:", self.outer_variable)
        self.inner_instance.show()  # 외부 클래스에서 이너 클래스의 메서드 호출

    class InnerClass:
        def __init__(self,outer):
            self.inner_variable = "This is from the inner class"
            self.outer = outer
        
        def show(self):
            print("Inside inner class:", self.inner_variable)
            self.outer.show_inner()
            

# 외부 클래스에서 이너 클래스에 접근
outer_object = OuterClass()
outer_object.show_inner()  # 외부 클래스 메서드에서 이너 클래스 메서드 호출
