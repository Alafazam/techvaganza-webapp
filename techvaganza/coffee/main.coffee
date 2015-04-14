$(document).on 'click', '#add_mod', ->
	data = {'cityname': $('#city-name-holder').text(),'firstname': $('#firstname_new').val(), 'lastname': $('#lastname_new').val(), 'email': $('#email_new').val()}
	$.getJSON('/addmoderators', data, (data, resp) -> 
		$("#mod-list").prepend("<tr><td>%f %l</td><td>%e</td><button type='button' class='btn btn-danger'>Remove Mod</button></td></tr>".replace('%f', $('#firstname_new').val()).replace('%l', $('#lastname_new').val()).replace('%e', $('#email_new').val()))
	)

$(document).on 'click', '.remove_mod', ->
	elem = $(this).parent().parent()
	email = $(this).parent().parent().find('.email').text()
	data = {'email' : email, 'cityname': $('#city-name-holder').text()}
	$.getJSON('/removemoderator', data, (data, resp) -> 
		elem.remove()
	)

$(document).on 'click', '#addRbutton', ->
	if $(this).text() == "Add Restaurant"
		$(this).text("Click Map to Add Restaurant")
	else
		$(this).text("Add Restaurant")

$(document).on 'click', '.addReviewRest', ->
	if $('.review').text() != " " or $('.review').text() != ""
		data = {'text': $('textarea#review').val(), 'restaurant': $('#restaurantname').text(), 'city': $('#cityname').text()}
		$.getJSON('/addrestaurantreview', data, (data, resp) -> 
			location.reload()
		)

$(document).on 'mouseenter', '.votable-image', ->
	window.src = $(this).find('img').attr('src')
	$(this).replaceWith('<div class="vote_bar"><div class="upvote"><span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span></div><div class="downvote"><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></div></div>')

$(document).on 'mouseleave', '.vote_bar', ->
	$(this).replaceWith('<a href="#" class="pull-left votable-image"><img src="%%replace%%" id="review_image" class="media-object" alt=""/></a>'.replace('%%replace%%', window.src))


$(document).on 'mouseenter', '.dishvotable-image', ->
	window.src = $(this).find('img').attr('src')
	$(this).replaceWith('<div class="dishvote_bar"><div class="dishupvote"><span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span></div><div class="dishdownvote"><span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span></div></div>')

$(document).on 'mouseleave', '.dishvote_bar', ->
	$(this).replaceWith('<a href="#" class="pull-left dishvotable-image"><img src="%%replace%%" id="review_image" class="media-object" alt=""/></a>'.replace('%%replace%%', window.src))

$(document).on 'click', '.upvote', ->
	data = {'cityname': $('#cityname').text(), 'restaurantname': $('#restaurantname').text(), 'reviewname': $(this).parent().parent().find('.reviewname').text(), 'reviewtext': $(this).parent().parent().find('.reviewtext').text(), 'action': 'upvote'}
	$.getJSON('/reviewaction', data, (data, resp) -> 
			location.reload()
	)

$(document).on 'click', '.remove-clicker', ->
	data = {'cityname': $('#cityname').text(), 'restaurantname': $('#restaurantname').text(), 'reviewname': $(this).parent().parent().parent().find('.reviewname').text(), 'reviewtext': $(this).parent().parent().parent().find('.reviewtext').text(), 'action': 'delete'}
	$.getJSON('/reviewaction', data, (data, resp) -> 
			location.reload()
	)

$(document).on 'click', '.downvote', ->
	data = {'cityname': $('#cityname').text(), 'restaurantname': $('#restaurantname').text(), 'reviewname': $(this).parent().parent().find('.reviewname').text(), 'reviewtext': $(this).parent().parent().find('.reviewtext').text(), 'action': 'downvote'}
	$.getJSON('/reviewaction', data, (data, resp) -> 
			location.reload()
	)

$(document).on 'click', '.addReviewDish', ->
	if $('textarea#review').val() != " " and $('textarea#review').val() != ""
		if $('.list-group .selected').text() != "" and $('.list-group .selected').text() != " "
			data = {'text': $('textarea#review').val(), 'restaurant': $('#restaurantname').text(), 'city': $('#cityname').text(), 'dishname': $('.list-group .selected').text()}
			console.log data
			$.getJSON('/adddishreview', data, (data, resp) -> 
				location.reload()
			)

$(document).on 'click', '.dishupvote', ->
	data = {'cityname': $('#cityname').text(), 'restaurantname': $('#restaurantname').text(), 'reviewname': $(this).parent().parent().find('.reviewname').text(), 'reviewtext': $(this).parent().parent().find('.reviewtext').text(), 'dishname': $('.list-group .selected').text(), 'action': 'upvote'}
	$.getJSON('/dishreviewaction', data, (data, resp) -> 
			location.reload()
	)

$(document).on 'click', '.dishremove-clicker', ->
	data = {'cityname': $('#cityname').text(), 'restaurantname': $('#restaurantname').text(), 'reviewname': $(this).parent().parent().parent().find('.reviewname').text(), 'reviewtext': $(this).parent().parent().parent().find('.reviewtext').text(), 'dishname': $('.list-group .selected').text(), 'action': 'delete'}
	$.getJSON('/dishreviewaction', data, (data, resp) -> 
			location.reload()
	)

$(document).on 'click', '.dishdownvote', ->
	data = {'cityname': $('#cityname').text(), 'restaurantname': $('#restaurantname').text(), 'reviewname': $(this).parent().parent().find('.reviewname').text(), 'reviewtext': $(this).parent().parent().find('.reviewtext').text(), 'dishname': $('.list-group .selected').text(), 'action': 'downvote'}
	console.log data
	$.getJSON('/dishreviewaction', data, (data, resp) -> 
			location.reload()
	)