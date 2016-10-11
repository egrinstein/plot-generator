function doubleClick(e) {
        $but_div = $(this).parents().eq(1);
        $grandpa = $but_div.parent();
        $greatgrandpa = $grandpa.parent();
        label1 = $(".current-item").attr('label');
        label2 = $but_div.attr('label');
        value = $(this).attr('value');
        $.get('/feedback/', { label1: label1,
                               label2: label2,
                               value:  value,
                               sim:0});
        
        
        $(this).attr("btn-similarity","0");
        $(this).attr("clicked",true);
        $all_clicked_buttons = $grandpa.find('.btn-feedback[clicked]');
        if ($all_clicked_buttons.length == 3) {
        	$all_clicked_buttons.removeAttr("btn-similarity");
        	$all_clicked_buttons.removeAttr("clicked");
            pop_to_back();
            pop_to_top();
        }
}

function singleClick(e) {   
        $daddy = $(this).parents().eq(1);
        $grandpa = $daddy.parent();
        $greatgrandpa = $grandpa.parent();
        label1 = $(".current-item").attr('label');
        label2 = $daddy.attr('label');
        value = $(this).attr('value');
        $.get('/feedback/', { label1: label1,
                               label2: label2,
                               value:  value,
                               sim:1});

        
        $(this).attr("btn-similarity","1");
        $(this).attr("clicked",true);
        $all_clicked_buttons = $grandpa.find('.btn-feedback[clicked]');
        if ($all_clicked_buttons.length == 3) {
        	$all_clicked_buttons.removeAttr("btn-similarity");
        	$all_clicked_buttons.removeAttr("clicked");
            pop_to_back();
            pop_to_top();
        }
        
        
        
}



function pop_to_top() {
    $to_pop = $(".backlog>").first();
    $a = $to_pop.find(">").first();
    href = $a.attr("href");
    
    $img = $a.find(">").first();
    label = $img.attr("alt");

    src = $img.attr("src");
    $compare = $(".comparison-item.col-md-5");
    
    $compare.attr("label",label);
    $img = $compare.find(".compare-img>");
    //$compare.attr("href",href);
    $img.attr("src",src);
    $img.attr("alt",label);
    $img.removeClass('tint');
    $to_pop.remove()
}

function pop_to_back(){
    $backlog = $(".backlog");
    $to_pop = $(".comparison-item.col-md-5");
    $to_back = $to_pop.find(".compare-img").clone();
    label = $to_back.find(">").attr("alt");
    href = '"../../label/'.concat(label).concat('"')
    $img = $to_back.find(">"); 
    img_div = '<div class="col-md-2"><a href='
    img_div = img_div.concat(href).concat('</a></div>')
    $img_div = $(img_div);
    $to_back.removeClass("compare-img");
    $img.addClass('tint');
    $img_div.find(">").append($img);
    $backlog.append($img_div);
}

$(document).ready(function() {
    if(window.location.href.indexOf("label") > -1) {
        pop_to_top();
    }

    $(".skip-button").click(function() {
  		pop_to_back();
  		pop_to_top();
	});

    $(".btn-feedback").click(function(e) {
        var that = this;
        setTimeout(function() {
            var dblclick = parseInt($(that).data('double'), 10);
            if (dblclick > 0) {
                $(that).data('double', dblclick-1);
            } else {
                singleClick.call(that, e);
            }
        }, 500);
    }).dblclick(function(e) {
        $(this).data('double', 2);
        doubleClick.call(this, e);
    });
})
