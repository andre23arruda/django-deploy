(function( $ ) {

	'use strict';

	var datatableInit = function() {
		var $table = $('#datatable-tabletools');

		$table.dataTable({
			sDom: $.fn.dataTable.defaults.sDom + "<'text-right mt-lg'T>",
			oTableTools: {
				aButtons: [
					{
						sExtends: 'print',
						sButtonText: 'Imprimir',
						sInfo: 'Por favor, aperte CTR+P para imprimir ou ESC para sair.'
					},
				]
			}
		});

	};

	$(function() {
		datatableInit();
	});

}).apply( this, [ jQuery ]);
