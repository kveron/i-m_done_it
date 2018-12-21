$(function scroll() {

	$(window).scroll(function() {
 
		if($(this).scrollTop() != 0) {
 
			$('.toTop').fadeIn();
 
		} 

		else {
 
			$('.toTop').fadeOut();
 
		}
 
	});
 
	$('.toTop').click(function() {
 
		$('body,html').animate({scrollTop:0},800);
 
	});
});

// function buttonClick(){
// 		if(flag != 0){
// 			$('.sendToUs').fadeOut();
// 			$('.sendToUsBackground').fadeIn();
// 		}
// 	}
// function buttonClick_1(){
// 		if(flag != 1){
// 			$('.sendToUs').fadeOut();
// 			$('.sendToUsBackground').fadeIn();
// 		}
// 	}

// function click(){
// 	$('.sendToUs').onclick(function() {
// 		// var flag = 0;
// 		$('.sendToUs').fadeOut();
// 		$('.sendToUsBackground').fadeIn();
// 	});
// }

// function send(){
// 	$('.button').onclick(function() { alert("Уважаемый Иван, ваше сообщение принято!");
// 	});
// }
// function onReady(){
// 	$('.sendToUs').fadeIn();
// 	// $('.sendToUsBackground').fadeOut();
// }

// $(document).ready(onReady);