function fadeIn() {
    var widget = document.querySelector('.spotify-widget');
    widget.classList.remove('fadeOut');
    widget.classList.add('fadeIn');
}

function fadeOut() {
    var widget = document.querySelector('.spotify-widget');
    widget.classList.remove('fadeIn');
    widget.classList.add('fadeOut');
}

function isElementOverflowing(element) {

	var overflowX = element.offsetWidth < element.scrollWidth,
		overflowY = element.offsetHeight < element.scrollHeight;
	return (overflowX || overflowY);
}

function wrapContentsInMarquee(element) {
	var marquee = document.createElement('marquee'),
  	contents = element.innerText;
    
    marquee.innerText = contents;
    element.innerHTML = '';
    element.appendChild(marquee);
}

function unwrapContentsFromMarquee(element) {
    contents = element.firstChild.innerText;
    element.removeChild(element.firstChild);
    element.innerText = contents;
}

function readyFn(jQuery) {
    var elements = document.getElementsByClassName("overflow");

    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];

        if (isElementOverflowing(element)) {
            wrapContentsInMarquee(element);
        } else if (element.hasChildNodes() && element.firstChild.nodeName == 'MARQUEE') {
            unwrapContentsFromMarquee(element);
        }
    }
}

$(document).ready(readyFn);
