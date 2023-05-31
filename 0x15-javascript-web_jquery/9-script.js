$(function () {
	$("body").ready(() => {
		$.getJSON("https://stefanbohacek.com/hellosalut/?lang=fr", (r) => {
			$("DIV#hello").text(`${r.hello}`);
		});
	});
});
