# 클래스

1. 클래스는 작아야 한다.

   함수와 마찬가지로 클래스의 크기가 너무 커지지 않도록 "작게 만드는 것"을 기본 원칙으로 해야 한다.

2. 이름이 너무 길어지는(최대 if, and, or, but을 사용하지 않고 25자 내외) 경우에는 하나의 클래스가 너무 많은 역할을 하는 것은 아닌지 의심해야한다.

   이는 단일 책임 원칙(Single Responsibility Principle)과도 연관된다.

3. 응집도가 높은 클래스를 사용하면 좋다.

   클래스가 가진 변수의 수는 적고, 각 메서드들이 내부 변수를 잘 활용하고 있을 때, 응집도가 높은 클래스라고 판단한다.

4. 변경하기 쉬운 형태여야한다.

   하나의 클래스 안에 모든 기능을 넣기 보다는 아래와 같이 작은 클래스로 쪼개어 미래의 변경에 대비해야한다.

   ```js
   class Person {
     constructor(name, age) {
       this.name = name;
       this.age = age;
     }
     
     think() { ... }
   }
     
   class Programmer extends Person {
     constructor(name, age, position) {
       super(name, age);
       this.position = position
     }
   }
   
   class Writer extends Person {
     constructor(name, age, theme) {
       super(name, age);
       this.theme = theme;
     }
   }
   ```

5. 메소드 체이닝을 활용해본다.

   클래스 내부 함수에서 `this`를 return하는 것만으로도 좋은 효과를 볼 수 있다.

   ```javascript
   class Tire {
     constructor(brand, size, vendor) {
       this.brand = brand;
       this.size = size;
       this.vendor = vendor;
     }
     
     setBrand(brand) {
       this.brand = brand;
       return this;
     }
     
     setSize(size) {
       this.size = size;
       return this;
     }
     
     setVendor(vendor) {
       this.vendor = vendor;
       return this;
     }
   }
   
   const tire = new Tire()
   	.setBrand('goodrich')
   	.setSize('225/45R17')
   	.setVendor('tirepro');
   ```
