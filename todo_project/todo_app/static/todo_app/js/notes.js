$(document).ready(() => {
	$('input[type="checkbox"][name="is_done"]').click(function () {
		let note_id = String($(this).data("note-id"));
		let note_form = $(this).parent();
		let note_title = $(note_form).children()[0];
		let note_status = $(this).is(":checked");

		$.ajax({
			url: "/mark_note/",
			type: "post",
			contentType: "application/json",
			data: JSON.stringify({ note_id: note_id, checked: note_status }),
			success: (response) => {
				if (note_status === true) {
					$(note_title).replaceWith('<s><span class="title">' + $(note_title).text() + '</span></s>');
				} else {
					$(note_title).replaceWith('<span class="title">' + $(note_title).text() + '</span>');
				}
			}
		})
	})
});


var options = {
	valueNames: ["title", "note_id"]

};

var hackerList = new List('mylist', options);