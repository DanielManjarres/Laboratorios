// 2. Clases Concretas de muebles
var ModernChair = /** @class */ (function () {
    function ModernChair() {
    }
    ModernChair.prototype.assemble = function () {
        console.log('Assembling modern chair');
    };
    return ModernChair;
}());
var VictorianChair = /** @class */ (function () {
    function VictorianChair() {
    }
    VictorianChair.prototype.assemble = function () {
        console.log('Assembling victorian chair');
    };
    return VictorianChair;
}());
var RusticChair = /** @class */ (function () {
    function RusticChair() {
    }
    RusticChair.prototype.assemble = function () {
        console.log('Assembling rustic chair');
    };
    return RusticChair;
}());
var ModernSofa = /** @class */ (function () {
    function ModernSofa() {
    }
    ModernSofa.prototype.recline = function () {
        console.log('Reclining modern sofa');
    };
    return ModernSofa;
}());
var VictorianSofa = /** @class */ (function () {
    function VictorianSofa() {
    }
    VictorianSofa.prototype.recline = function () {
        console.log('Reclining victorian sofa');
    };
    return VictorianSofa;
}());
var RusticSofa = /** @class */ (function () {
    function RusticSofa() {
    }
    RusticSofa.prototype.recline = function () {
        console.log('Reclining rustic sofa');
    };
    return RusticSofa;
}());
var ModernTable = /** @class */ (function () {
    function ModernTable() {
    }
    ModernTable.prototype.assemble = function () {
        console.log('Assembling modern table');
    };
    return ModernTable;
}());
var VictorianTable = /** @class */ (function () {
    function VictorianTable() {
    }
    VictorianTable.prototype.assemble = function () {
        console.log('Assembling victorian table');
    };
    return VictorianTable;
}());
var RusticTable = /** @class */ (function () {
    function RusticTable() {
    }
    RusticTable.prototype.assemble = function () {
        console.log('Assembling rustic table');
    };
    return RusticTable;
}());
// 4. Clases Concretas de Fábricas
var ModernFurnitureFactory = /** @class */ (function () {
    function ModernFurnitureFactory() {
    }
    ModernFurnitureFactory.prototype.createChair = function () {
        return new ModernChair();
    };
    ModernFurnitureFactory.prototype.createSofa = function () {
        return new ModernSofa();
    };
    ModernFurnitureFactory.prototype.createTable = function () {
        return new ModernTable();
    };
    return ModernFurnitureFactory;
}());
var VictorianFurnitureFactory = /** @class */ (function () {
    function VictorianFurnitureFactory() {
    }
    VictorianFurnitureFactory.prototype.createChair = function () {
        return new VictorianChair();
    };
    VictorianFurnitureFactory.prototype.createSofa = function () {
        return new VictorianSofa();
    };
    VictorianFurnitureFactory.prototype.createTable = function () {
        return new VictorianTable();
    };
    return VictorianFurnitureFactory;
}());
var RusticFurnitureFactory = /** @class */ (function () {
    function RusticFurnitureFactory() {
    }
    RusticFurnitureFactory.prototype.createTable = function () {
        return new RusticTable();
    };
    RusticFurnitureFactory.prototype.createChair = function () {
        return new RusticChair();
    };
    RusticFurnitureFactory.prototype.createSofa = function () {
        return new RusticSofa();
    };
    return RusticFurnitureFactory;
}());
// 5. Código Cliente
function main(factory) {
    var chair = factory.createChair();
    var sofa = factory.createSofa();
    var table = factory.createTable();
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
