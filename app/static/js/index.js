// window.onload = function() {

function getRandom(min, max) {
    return Math.random() * (max - min) + min;
}

// $("h1").blast({
//     delimiter: "character"
// });

$("#logo").hover(function(argument) {
    $('.logo')
        .velocity({
            opacity: 0
        }, 0)
        .velocity({
            opacity: 1
        }, {
            duration: 2650,
            delay: 10
        });

    $('.path')
        // .velocity('stop', true)
        .velocity({            
            'stroke-dashoffset': 400,
            'stroke-dasharray': 200
        }, 0)
        .velocity({
            'stroke-dashoffset': 0
        }, {
            duration: 2650,
            delay: 10
        });
    // console.log("bogie");

}, function(argument) {
    // body...
});

// // Run the animation on click
// $('.button').on('click', function(){
//   animate();
// });

function animate() {}
    // };
