let cards = ['Jack', 8, 2, 6, 'King', 5, 3, 'Queen'];


let theRightOrder = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"];

cards.sort((a, b) => theRightOrder.indexOf(a) - theRightOrder.indexOf(b));
let card1=['Jack', 8, 2, 6, 5, 3]
card1.sort((a,b))  

console.log(card1);