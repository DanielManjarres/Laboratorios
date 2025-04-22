// 1. Interfaces abstractas de productos
interface AbstractProductA {
    operationA(): void;
}
  
interface AbstractProductB {
    operationB(): void;
}
  
// 2. Productos concretos para la familia 1
class ConcreteProductA1 implements AbstractProductA {
    operationA(): void {
    console.log('Operation from ConcreteProductA1');
    }
}
  
class ConcreteProductB1 implements AbstractProductB {
    operationB(): void {
        console.log('Operation from ConcreteProductB1');
    }
}
  
// 3. Productos concretos para la familia 2
class ConcreteProductA2 implements AbstractProductA {
    operationA(): void {
        console.log('Operation from ConcreteProductA2');
    }
}

class ConcreteProductB2 implements AbstractProductB {
    operationB(): void {
        console.log('Operation from ConcreteProductB2');
    }
}

// 4. Interfaz de la Fábrica Abstracta
interface AbstractFactory {
    createProductA(): AbstractProductA;
    createProductB(): AbstractProductB;
}

// 5. Fábrica concreta 1
class ConcreteFactory1 implements AbstractFactory {
    createProductA(): AbstractProductA {
        return new ConcreteProductA1();
    }

    createProductB(): AbstractProductB {
        return new ConcreteProductB1();
    }
}

// 6. Fábrica concreta 2
class ConcreteFactory2 implements AbstractFactory {
    createProductA(): AbstractProductA {
        return new ConcreteProductA2();
    }

    createProductB(): AbstractProductB {
        return new ConcreteProductB2();
    }
}

// 7. Código Cliente
class Client {
    private productA: AbstractProductA;
    private productB: AbstractProductB;

    constructor(factory: AbstractFactory) {
        this.productA = factory.createProductA();
        this.productB = factory.createProductB();
    }

    someOperation(): void {
        this.productA.operationA();
        this.productB.operationB();
    }
}

// 8. Pruebas
console.log('Using ConcreteFactory1:');
const client1 = new Client(new ConcreteFactory1());
client1.someOperation();

console.log('\nUsing ConcreteFactory2:');  
const client2 = new Client(new ConcreteFactory2());
client2.someOperation();
  