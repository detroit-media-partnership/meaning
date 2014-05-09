$(function() {
	$('.sliders').slider({
		"min": 0,
		"max": 100,
		"value": 50
	}).on("slide", function(ev) {
		$("#" + ev.target.id).parent().parent().parent().find(".slider-value").html("Value: " + $("#" + ev.target.id).data("slider").getValue());
	});
});
