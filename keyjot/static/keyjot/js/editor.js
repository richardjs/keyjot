'use strict';

// Initialize the editor
var editor = new EpicEditor({
	basePath: EPICEDITOR_BASE,
	clientSideStorage: false,
	focusOnLoad: true
}).load();

// Load the file form the server
function loadFile(){
	$.get(window.location + '/get', function(data){
		editor.importFile(filename, data);
	});
}

// Save the file on the server
function saveFile(){
	var fileData = editor.exportFile();
	$.post(window.location + '/save', {
		data: fileData,
		csrfmiddlewaretoken: csrf_token
	}, function(data){
		if(data === 'ok'){
			alert('Saved!')
		}else{
			alert('Error saving!')
		}
	});
}

// Load the file
loadFile();

// Resize the editor to fit the window size
function resizeEditor(){
	$(editor.getElement('container')).css('height', (window.innerHeight) + 'px');
	editor.reflow();
}
resizeEditor();
$(window).on('resize', resizeEditor);

// Keyboard shortcuts
$([editor.editorIframeDocument, editor.previewerIframeDocument]).on('keypress', function(event){
	if(!event.altKey){
		return;
	}

	switch(event.key){
		case 'o':
			event.preventDefault();
			var toOpen = prompt('Name to open?');
			if(toOpen.length){
				window.location = toOpen;
			}
		case 'l':
			event.preventDefault();
			if(confirm('Really reload from server?')){
				loadFile();
			}
			break;
		case 's':
			event.preventDefault();
			saveFile();
			break;
	}
});
