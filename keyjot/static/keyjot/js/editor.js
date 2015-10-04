'use strict';

// Initialize the editor
var editor = new EpicEditor({
	basePath: EPICEDITOR_BASE,
	clientSideStorage: false,
	focusOnLoad: true
}).load();

$.get(window.location + '/get', function(data){
	editor.importFile(filename, data);
});

// Resize the editor to fit the window size
function resizeEditor(){
	$(editor.getElement('container')).css('height', (window.innerHeight) + 'px');
	editor.reflow();
}
resizeEditor();
$(window).on('resize', resizeEditor);
