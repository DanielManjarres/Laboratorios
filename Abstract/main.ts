// 1. Interfaces de Chair y Sofa
interface Chair {
  assemble(): void;
}

interface Sofa {
  recline(): void;
}

interface Table {
  assemble(): void;
}

// 2. Clases Concretas de muebles

class ModernChair implements Chair {
  assemble(): void {
    console.log('Assembling modern chair');
  }
}

class VictorianChair implements Chair {
  assemble(): void {
    console.log('Assembling victorian chair');
  }
}

class RusticChair implements Chair {
  assemble(): void {
    console.log('Assembling rustic chair');
  }
}

class ModernSofa implements Sofa {
  recline(): void {
    console.log('Reclining modern sofa');
  }
}

class VictorianSofa implements Sofa {
  recline(): void {
    console.log('Reclining victorian sofa');
  }
}

class RusticSofa implements Sofa {
  recline(): void {
    console.log('Reclining rustic sofa');
  }
}

class ModernTable implements Table {
  assemble(): void {
    console.log('Assembling modern table');
  }
}

class VictorianTable implements Table {
  assemble(): void {
    console.log('Assembling victorian table');
  }
}

class RusticTable implements Table {
  assemble(): void {
    console.log('Assembling rustic table');
  }
}

// 3. Interfaz de la Fábrica Abstracta

interface FurnitureFactory {
  createChair(): Chair;
  createSofa(): Sofa;
  createTable(): Table;
}

// 4. Clases Concretas de Fábricas
class ModernFurnitureFactory implements FurnitureFactory {
  createChair(): Chair {
    return new ModernChair();
  }

  createSofa(): Sofa {
    return new ModernSofa();
  }
  createTable(): Table {
    return new ModernTable();
  }
}

class VictorianFurnitureFactory implements FurnitureFactory {
  createChair(): Chair {
    return new VictorianChair();
  }
  createSofa(): Sofa {
    return new VictorianSofa();
  }
  createTable(): Table {
    return new VictorianTable();
  }
}

class RusticFurnitureFactory implements FurnitureFactory {
  createTable(): Table {
    return new RusticTable();
  }
  createChair(): Chair {
    return new RusticChair();
  }
  createSofa(): Sofa {
    return new RusticSofa();
  }
}

// 5. Código Cliente

function main(factory: FurnitureFactory) {
  const chair = factory.createChair();
  const sofa = factory.createSofa();
  const table = factory.createTable();

  chair.assemble();
  sofa.recline();
  table.assemble();
}

// Pruebas
console.log('Creating modern furniture:');
main(new ModernFurnitureFactory());

console.log('\nCreating victorian furniture:');
main(new VictorianFurnitureFactory());

console.log('\nCreating rustic furniture:');
main(new RusticFurnitureFactory());