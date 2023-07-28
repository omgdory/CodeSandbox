class Pawn {
    constructor(attack, defense) {
        this.attack = attack
        this.defense = defense
    }

    handleAttack(other, seed) {
        var affectValue = Math.floor(this.attack * seed)
        other.defense -= affectValue
        this.attack -= affectValue
    }
}

// false = player 1
// true = player 2
let currentTurn = false

// Display variables (display on page)
let displayAttackP1 = document.getElementById("AttackP1")
let displayDefenseP1 = document.getElementById("DefenseP1")
let displayAttackP2 = document.getElementById("AttackP2")
let displayDefenseP2 = document.getElementById("DefenseP2")

// initialization vars
const seed = 7
const minAtt = 2
const minDef = 2


let generateAttack = (seed) => {
    return Math.floor(Math.random()*seed) + minAtt
}

let generateDefense = (seed) => {
    return Math.floor(Math.random()*seed) + minDef
}

let pawn1 = new Pawn(generateAttack(seed), generateDefense(seed))
let pawn2 = new Pawn(generateAttack(seed), generateDefense(seed))

window.onload = function() {
    displayAttackP1.innerHTML = pawn1.attack
    displayDefenseP1.innerHTML = pawn1.defense

    displayAttackP2.innerHTML = pawn2.attack
    displayDefenseP2.innerHTML = pawn2.defense    
}

let reset = () => {

}

let gameLoop = () => {

}
