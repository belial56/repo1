window.dhx4.skin = 'dhx_web';
	var main_layout = new dhtmlXLayoutObject(document.body, '3E');

	var a = main_layout.cells('a');
	var toolbar_1 = a.attachToolbar();
	toolbar_1.setIconsPath('./codebase/imgs/');
	
	toolbar_1.loadStruct('<toolbar><item type="button" id="add_b" text="добавить" /><item type="button" id="delete_b" text="Удалить" /></toolbar>', function() {});

