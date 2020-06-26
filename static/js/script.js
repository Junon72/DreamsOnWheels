$(document).ready(function () {

	// Sticky Navigation
	window.onscroll = function () {
		myFunction();
	};

	var header = document.getElementById('dowHeader');
	var sticky = header.offsetTop;

	function myFunction() {
		if (window.pageYOffset > sticky) {
			header.classList.add('sticky');
		} else {
			header.classList.remove('sticky');
		}
	}

	// Tooltips
	$(function () {
		$('[data-tooltip="tooltip"]').tooltip();
	});

	//Sales Carousel - Slick
	$('.responsive').slick({
		dots: true,
		infinite: true,
		speed: 300,
		nextArrow: $('.next'),
		prevArrow: $('.prev'),
		mobileFirst: true,
		responsive: [{
				breakpoint: 1400,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 4,
					infinite: true,
					dots: true
				}
			},
			{
				breakpoint: 1020,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 3,
					infinite: true,
					dots: true
				}
			},
			{
				breakpoint: 600,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 2
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}
			// You can unslick at a given breakpoint now by adding:
			// settings: "unslick"
			// instead of a settings object
		]
	});

	// Hide alert messages timer
	$(".alert").fadeTo(2500, 500).slideUp(500, function () {
		$(".alert").slideUp(500);
	});

	// Highlight Carousel top - Bootstrap4
	$('.carousel').carousel();

	// Hide / Show Comments section in blog post and
	// keep the element class after page reload
	// Resource: https://stackoverflow.com/questions/55819969/keep-class-toggled-after-page-refresh
	// Check if section-state in localStorage and get
	// the stored hidden/ show state of Comments section
	if (
		localStorage.getItem('section-state') &&
		localStorage.getItem('section-state') === 'true'
	) {
		$('#commentSection').addClass('show');
	}
	// Toggle the comment section hidden/ shown state
	$('#commentsToggle').click(function() {
    let el = $('#commentSection');
	el.toggleClass('show');
	// Register hidden/ show state in localStorage
    localStorage.setItem('section-state', el.hasClass('show'));
  });

	// Autofocus to first input field of a modal forms
	$('.modal').on('shown.bs.modal', function () {
		$('form').find('input[type=text').filter(':visible:first').focus();
	});
}); 