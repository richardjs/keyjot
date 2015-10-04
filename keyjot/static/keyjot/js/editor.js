'use strict';

// Initialize the editor
var editor = new EpicEditor({
	basePath: EPICEDITOR_BASE,
	clientSideStorage: false,
	focusOnLoad: true
}).load();

// Resize the editor to fit the window size
function resizeEditor(){
	editor.getElement('container').style.height = (window.innerHeight) + 'px';
	editor.reflow();
}
resizeEditor();
window.addEventListener('resize', resizeEditor);
