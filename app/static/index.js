dhtmlx.image_path='./codebase/imgs/';

	var main_layout = new dhtmlXLayoutObject(document.body, '3L', 'dhx_skyblue');

	var a = main_layout.cells('a');
	a.setText('Главная');
	a.setWidth('250');
	var str = [
		{ type:"settings" , labelWidth:80, inputWidth:250, position:"absolute"  },
		{ type:"label" , name:"form_label_1", label:"Авторы", width:250, labelWidth:250, labelAlign:"left", labelLeft:25, labelTop:5  },
		{ type:"label" , name:"form_label_2", label:"Книги", width:250, labelWidth:250, labelAlign:"left", labelLeft:25, labelTop:50  }
	];

	var form_1 = a.attachForm(str);




	var b = main_layout.cells('b');
	b.setText('Авторы');
	var grid_1 = b.attachGrid();
	grid_1.setIconsPath('./codebase/imgs/');
	
	grid_1.setHeader(["id","Автор","Дата рождения",""]);
	grid_1.setColTypes("ro,ro,ro,ro");
	
	grid_1.setColSorting('str,str,str,str');
	grid_1.enableValidation(true, false);
grid_1.setColValidators('ValidInteger,,ValidDate,');
	grid_1.setColWidth(0, '20');
	grid_1.init();
	grid_1.load('./data/grid.xml', 'xml');
	
	var toolbar_1 = b.attachToolbar();
	toolbar_1.setIconsPath('./codebase/imgs/');
	
	toolbar_1.loadStruct('<toolbar><item type="button" id="add" text="Добавить" title="Добавить автора" /><item type="button" id="delete" text="Удалить" title="Удалить автора" /></toolbar>', function(){});


	var c = main_layout.cells('c');
	c.setText('Книги');
	var grid_2 = c.attachGrid();
	grid_2.setIconsPath('./codebase/imgs/');
	
	grid_2.setHeader(["id","Название","Автор","Жанр","Column 5"]);
	grid_2.setColTypes("ro,ro,ro,ro,ro");
	
	grid_2.setColSorting('str,str,str,str,str');
	grid_2.enableValidation(true, false);
grid_2.setColValidators('ValidInteger,,ValidDate,,');
	grid_2.setColWidth(0, '20');
	grid_2.init();
	grid_2.load('./data/grid.xml', 'xml');
	
	var toolbar_2 = c.attachToolbar();
	toolbar_2.setIconsPath('./codebase/imgs/');
	
	toolbar_2.loadStruct('<toolbar><item type="button" id="add_book" text="Добавить" img="" imgdis="" title="Добавить запись" /><item type="button" id="delete_book" text="Удалить" title="Удалить запись" /></toolbar>', function(){});



	var windows = new dhtmlXWindows();
	windows.setSkin('dhx_skyblue');

	var add_auth = windows.createWindow('add_auth', 460, 400, 600, 150);
	var str = [
		{ type:"settings" , labelWidth:80, inputWidth:250, position:"absolute"  },
		{ type:"calendar" , name:"form_calendar_1", label:"Дата рождения", labelWidth:250, options:{
			
		}, labelLeft:300, labelTop:5, inputLeft:300, inputTop:21  },
		{ type:"input" , name:"form_input_1", label:"Имя автора", labelWidth:250, labelLeft:25, labelTop:5, inputLeft:25, inputTop:21  },
		{ type:"button" , name:"form_button_1", label:"Добавить", value:"Добавить", width:"250", inputLeft:175, inputTop:50  }
	];

	var form_2 = add_auth.attachForm(str);



	add_auth.setText('Добавить автора');
	add_auth.denyResize();
	add_auth.centerOnScreen();
	add_auth.button('park').hide();
	add_auth.button('minmax1').hide();


	var add_book = windows.createWindow('add_book', 400, 400, 800, 150);
	var str = [
		{ type:"settings" , labelWidth:80, inputWidth:250, position:"absolute"  },
		{ type:"input" , name:"form_input_2", label:"Название", labelWidth:250, labelLeft:25, labelTop:5, inputLeft:25, inputTop:21  },
		{ type:"input" , name:"form_input_3", label:"Автор", labelWidth:250, labelLeft:300, labelTop:5, inputLeft:300, inputTop:21  },
		{ type:"combo" , name:"genres", label:"Жанр", labelWidth:175, inputWidth:175, labelLeft:575, labelTop:5, inputLeft:575, inputTop:21, options:[
					{ value:"Роман", text:"Роман" },
		{ value:"Фэнтези", text:"Фэнтези" },
		{ value:"Детектив", text:"Детектив" },
		{ value:"Фантастика", text:"Фантастика" },
		{ value:"Стихи", text:"Стихи" },
		{ value:"Приключения", text:"Приключения" }
			]  },
		{ type:"button" , name:"form_button_2", label:"Добавить", value:"Добавить", width:"250", inputLeft:250, inputTop:50  }
	];

	var form_3 = add_book.attachForm(str);



	add_book.setText('Добавить книгу');
	add_book.denyResize();
	add_book.centerOnScreen();
	add_book.button('stick').hide();
	add_book.button('park').hide();
	add_book.button('minmax1').hide();



