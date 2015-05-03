function getRandom(min, max) {
    return Math.random() * (max - min) + min;
}

$("h1").blast({
    delimiter: "character"
});

$("#tv").hover(
    function() {
        var $spans = $(this).find('span');
        var p = getRandom(-1, 1) > 0 ? 1 : -1;
        $spans.each(function(val) {
            $(this).velocity('stop',true);
            var z = (val % 2) > 0 ? -1 : 1;
            z *= p;
            var w = 0;
            if (val == 0) {
                z = 0;
                w = -2;
            };
            if (val == 12) {
                z = 0;
                w = +2;
            };

            var scale = getRandom(.5, 1.5);
            // if (val == 6) {
            //     z = 0;
            //     scale = 1;
            // };
            var offsetY = 100 * z;
            var offsetX = getRandom(30, 50) * w;
            $(this).velocity({
                translateX: offsetX,
                translateY: offsetY,
                scale: scale,
                color: '#990000'
            }, {
                duration: 400,
                easing: "spring",
                loop: false,
                delay: "",
                mobileHA: true
            });

        });
        $('.soon').velocity('stop',true);
        $('.soon').velocity({
            opacity: 1
        }, {
            display: "block"
        }, {
            duration: 300,
            easing: "spring",
        });
    },
    function() {
        var self = $(this);
        var $spans = $(this).find('span');
        $spans.each(function(val, el) {
            $(this).velocity({translateX: 0,translateY: 0,scale: 1,color: '#000'}, 200);
            // $(this).velocity("reverse");
        });
        $('.soon').velocity({opacity: 0}, {display: "none"},{duration: 300,easing: "spring"});
        // $('.soon').velocity('reverse');
        // velocity('finish');

    }
);
