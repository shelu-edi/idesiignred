// Variables

let ladies_sub = document.getElementById('ladies-sub');
let boys_sub = document.getElementById('boys-sub');
let girls_sub = document.getElementById('girls-sub');
let infants_sub = document.getElementById('infants-sub');
let teens_sub = document.getElementById('teens-sub');

let ladies_main = document.getElementById('ladies-main');
let boys_main = document.getElementById('boys-main');
let girls_main = document.getElementById('girls-main');
let infants_main = document.getElementById('infants-main');
let teens_main = document.getElementById('teens-main');

let ladies_table_wrapper = document.getElementById('ladies-tables-wrapper');
let boys_table_wrapper = document.getElementById('boys-tables-wrapper');
let girls_table_wrapper = document.getElementById('girls-table-wrapper');
let infants_table_wrapper = document.getElementById('infant-table-wrapper');
let teens_table_wrapper = document.getElementById('teens-tables-wrapper');

// Ladies
let ladies_frock = document.getElementById('ladies-frock');
let ladies_blouse = document.getElementById('ladies-blouse');
let ladies_pant = document.getElementById('ladies-pant');
let ladies_skirt = document.getElementById('ladies-skirt');
let ladies_tshirt = document.getElementById('ladies-tshirt');
let maternity_frock = document.getElementById('maternity-frock');
let ladies_kaftan = document.getElementById('kaftan');
let ladies_nightwear = document.getElementById('nightwear');

// Boys
let boys_pant = document.getElementById('boys-pant');
let boys_shirt = document.getElementById('boys-shirt');
let boys_tshirt = document.getElementById('boys-tshirt');
let boys_short = document.getElementById('boys-short');

let boys_pant_table = document.getElementById('boys-pant-table');
let boys_shirt_table = document.getElementById('boys-shirt-table');
let boys_tshirt_table = document.getElementById('boys-tshirt-table');
let boys_short_table = document.getElementById('boys-short-table');

let boys_pant_top = document.getElementById('boys-pant-top');
let boys_shirt_top = document.getElementById('boys-shirt-top');
let boys_tshirt_top = document.getElementById('boys-tshirt-top');
let boys_short_top = document.getElementById('boys-short-table');

// Girls
let girls_frock = document.getElementById('girls-frock');
let girls_pant = document.getElementById('girls-pant');
let girls_tshirt = document.getElementById('girls-tshirt');
let girls_short = document.getElementById('girls-short');

let girls_frock_table = document.getElementById('girls-frock-table');
let girls_pant_table = document.getElementById('girls-pant-table');
let girls_tshirt_table = document.getElementById('girls-tshirt-table');
let girls_short_table = document.getElementById('girls-short-table');

let girls_frock_top = document.getElementById('girls-frock-top');
let girls_pant_top = document.getElementById('girls-pant-top');
let girls_tshirt_top = document.getElementById('girls-tshirt-top');
let girls_short_top = document.getElementById('girls-short-top');

function LadiesSub() {

    // Sub Categories
    ladies_sub.style.display = 'flex';
    boys_sub.style.display = 'none';
    girls_sub.style.display = 'none';
    infants_sub.style.display = 'none';
    teens_sub.style.display = 'none';

    // Main Categories
    ladies_main.style.background = '#072D75';
    boys_main.style.background = 'white';
    girls_main.style.background = 'white';
    infants_main.style.background = 'white';
    teens_main.style.background = 'white';

    ladies_main.style.color = '#fff';
    boys_main.style.color = '#072D75';
    girls_main.style.color = '#072D75';
    infants_main.style.color = '#072D75';
    teens_main.style.color = '#072D75';

    // Wrappers
    ladies_table_wrapper.style.display = 'block';
    boys_table_wrapper.style.display = 'none';
    girls_table_wrapper.style.display = 'none';
    infants_table_wrapper.style.display = 'none';
    teens_table_wrapper.style.display = 'none';
}

function BoysSub() {
    // Sub Categories
    boys_sub.style.display = 'flex';
    ladies_sub.style.display = 'none';
    girls_sub.style.display = 'none';
    infants_sub.style.display = 'none';
    teens_sub.style.display = 'none';

    // Main Categories
    boys_main.style.background = '#072D75';
    ladies_main.style.background = 'white';
    girls_main.style.background = 'white';
    infants_main.style.background = 'white';
    teens_main.style.background = 'white';

    boys_main.style.color = '#fff';
    ladies_main.style.color = '#072D75';
    girls_main.style.color = '#072D75';
    infants_main.style.color = '#072D75';
    teens_main.style.color = '#072D75';

    //boys sub
    boys_pant.style.background = '#072D75';
    boys_shirt.style.background = 'white';
    boys_tshirt.style.background = 'white';
    boys_short.style.background = 'white';

    boys_pant.style.color = '#fff'

    // boys tables
    boys_pant_table.style.display = 'block';
    boys_shirt_table.style.display = 'none';
    boys_tshirt_table.style.display = 'none';
    boys_short_table.style.display = 'none';

    // Wrappers
    boys_table_wrapper.style.display = 'block';
    ladies_table_wrapper.style.display = 'none';
    girls_table_wrapper.style.display = 'none';
    infants_table_wrapper.style.display = 'none';
    teens_table_wrapper.style.display = 'none';

    //top
    boys_pant_top.style.display = 'block';
    boys_shirt_top.style.display = 'none';
    boys_tshirt_top.style.display = 'none';
    boys_short_top.style.display = 'none';
}

function GirlsSub() {
    // Sub Categories
    girls_sub.style.display = 'flex';
    ladies_sub.style.display = 'none';
    boys_sub.style.display = 'none';
    infants_sub.style.display = 'none';
    teens_sub.style.display = 'none';

    // Main Categories
    girls_main.style.background = '#072D75';
    ladies_main.style.background = 'white';
    boys_main.style.background = 'white';
    infants_main.style.background = 'white';
    teens_main.style.background = 'white';

    girls_main.style.color = '#fff';
    ladies_main.style.color = '#072D75';
    boys_main.style.color = '#072D75';
    infants_main.style.color = '#072D75';
    teens_main.style.color = '#072D75';

    // Girls Sub
    girls_frock.style.background = '#072D75';
    girls_pant.style.background = 'white';
    girls_tshirt.style.background = 'white';
    girls_short.style.background = 'white';

    girls_frock.style.color = '#fff';

    // Girls Table
    girls_frock_table.style.display = 'block';
    girls_pant_table.style.display = 'none';
    girls_tshirt_table.style.display = 'none';
    girls_short_table.style.display = 'none';

    // Wrappers
    girls_table_wrapper.style.display = 'block';
    ladies_table_wrapper.style.display = 'none';
    boys_table_wrapper.style.display = 'none';
    infants_table_wrapper.style.display = 'none';
    teens_table_wrapper.style.display = 'none';

    //top
    girls_frock_top.style.display = 'block';
    girls_pant_top.style.display = 'none';
    girls_tshirt_top.style.display = 'none';
    girls_short_top.style.display = 'none';
}

function InfantsSub() {
    // Sub Categories
    document.getElementById('infants-sub').style.display = 'flex';
    document.getElementById('ladies-sub').style.display = 'none';
    document.getElementById('boys-sub').style.display = 'none';
    document.getElementById('girls-sub').style.display = 'none';
    document.getElementById('teens-sub').style.display = 'none';

    // Main Categories
    document.getElementById('infants-main').style.background = '#072D75';
    document.getElementById('ladies-main').style.background = 'white';
    document.getElementById('boys-main').style.background = 'white';
    document.getElementById('girls-main').style.background = 'white';
    document.getElementById('teens-main').style.background = 'white';

    document.getElementById('infants-main').style.color = '#fff';
    document.getElementById('ladies-main').style.color = '#072D75';
    document.getElementById('boys-main').style.color = '#072D75';
    document.getElementById('girls-main').style.color = '#072D75';
    document.getElementById('teens-main').style.color = '#072D75';

    // Infant Sub
    document.getElementById('infants-frock').style.background = '#072D75';
    document.getElementById('infants-pant').style.background = 'white';

    document.getElementById('infants-frock').style.color = '#fff';

    // Tables
    document.getElementById('infant-frock-table').style.display = 'block';
    document.getElementById('infant-pant-table').style.display = 'none';

    // Wrappers
    document.getElementById('infant-table-wrapper').style.display = 'block';
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
    document.getElementById('girls-table-wrapper').style.display = 'none';
    document.getElementById('boys-tables-wrapper').style.display = 'none';
    document.getElementById('teens-tables-wrapper').style.display = 'none';

    // top
    document.getElementById('infants-frock-top').style.display = 'block';
    document.getElementById('infants-pant-top').style.display = 'none';
}

function TeensSub() {
    // Sub Categories
    document.getElementById('teens-sub').style.display = 'flex';
    document.getElementById('ladies-sub').style.display = 'none';
    document.getElementById('boys-sub').style.display = 'none';
    document.getElementById('girls-sub').style.display = 'none';
    document.getElementById('infants-sub').style.display = 'none';

    // Main Categories
    document.getElementById('teens-main').style.background = '#072D75';
    document.getElementById('ladies-main').style.background = 'white';
    document.getElementById('boys-main').style.background = 'white';
    document.getElementById('girls-main').style.background = 'white';
    document.getElementById('infants-main').style.background = 'white';

    document.getElementById('teens-main').style.color = '#fff';
    document.getElementById('ladies-main').style.color = '#072D75';
    document.getElementById('boys-main').style.color = '#072D75';
    document.getElementById('girls-main').style.color = '#072D75';
    document.getElementById('infants-main').style.color = '#072D75';

    // Teens Sub
    document.getElementById('teens-frock').style.background = '#072D75';

    document.getElementById('teens-frock').style.color = '#fff';

    // Table
    document.getElementById('teens-frock-table').style.display = 'block';

    // Wrappers
    document.getElementById('teens-tables-wrapper').style.display = 'block';
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
    document.getElementById('girls-table-wrapper').style.display = 'none';
    document.getElementById('boys-tables-wrapper').style.display = 'none';
    document.getElementById('infant-table-wrapper').style.display = 'none';

    //sub
    document.getElementById('teens-frock-top').style.display = 'block';
}

function LadiesFrock() {
    //tables
    document.getElementById('ladies-frock-table').style.display = 'block';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-skirt-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('ladies-frock').style.background = '#072D75';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    ladies_frock.style.color = '#fff';
    ladies_blouse.style.color = '#072D75';
    ladies_pant.style.color = '#072D75';
    ladies_skirt.style.color = '#072D75';
    ladies_tshirt.style.color = '#072D75';
    maternity_frock.style.color = '#072D75';
    ladies_kaftan.style.color = '#072D75';
    ladies_nightwear.style.color = '#072D75';


    //top
    document.getElementById('ladies-frock-top').style.display = 'block';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';
}

function LadiesFrockDisplayForm() {
    document.getElementById('ladies-frock-form').style.display = 'block';
}

function LadiesFrockCloseForm() {
    document.getElementById('ladies-frock-form').style.display = 'none';
}

function Del_Itm() {
    let checkBox = document.getElementById('chbx');
    let div = document.getElementById('del-div')
    let top = document.getElementById('ladies-frock-top')

    if (checkBox.checked === true) {
        console.log('blah')
        div.style.display = 'block';
        top.style.display = 'none';
    } else {
        top.style.display = 'block';
        div.style.display = 'none';
    }
}

function LadiesBlouse() {
    //table
    document.getElementById('ladies-blouse-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('ladies-blouse').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    //top
    document.getElementById('ladies-blouse-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';

}

function LadiesBlouseDisplayForm() {
    document.getElementById('ladies-blouse-form').style.display = 'block';
}

function LadiesBlouseCloseForm() {
    document.getElementById('ladies-blouse-form').style.display = 'none';
}

function LadiesPant() {
    //table
    document.getElementById('ladies-pant-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-skirt-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('ladies-pant').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    //top
    document.getElementById('ladies-pant-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';
}

function LadiesPantDisplayForm() {
    document.getElementById('ladies-pant-form').style.display = 'block';
}

function LadiesPantCloseForm() {
    document.getElementById('ladies-pant-form').style.display = 'none';
}

function LadiesSkirt() {
    //table
    document.getElementById('ladies-skirt-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('ladies-skirt').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    //top
    document.getElementById('ladies-skirt-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';

}

function LadiesSkirtDisplayForm() {
    document.getElementById('ladies-skirt-form').style.display = 'block';
}

function LadiesSkirtCloseForm() {
    document.getElementById('ladies-skirt-form').style.display = 'none';
}

function LadiesTshirt() {
    //table
    document.getElementById('ladies-tshirt-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-skirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('ladies-tshirt').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    //top
    document.getElementById('ladies-tshirt-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';
}

function LadiesTshirtDisplayForm() {
    document.getElementById('ladies-tshirt-form').style.display = 'block';
}

function LadiesTshirtCloseForm() {
    document.getElementById('ladies-tshirt-form').style.display = 'none';
}

function MaternityFrock() {
    //table
    document.getElementById('maternity-frock-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-skirt-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('maternity-frock').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    //top
    document.getElementById('maternity-frock-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';
}

function MaternityFrockDisplayForm() {
    document.getElementById('maternity-frock-form').style.display = 'block';
}

function MaternityFrockCloseForm() {
    document.getElementById('maternity-frock-form').style.display = 'none';
}


function Kaftan() {
    //table
    document.getElementById('kaftan-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-skirt-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('kaftan').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

    //top
    document.getElementById('kaftan-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('nightwear-top').style.display = 'none';
}

function KaftanDisplayForm() {
    document.getElementById('kaftan-form').style.display = 'block';
}

function KaftanCloseForm() {
    document.getElementById('kaftan-form').style.display = 'none';
}

function Nightwear() {
    //table
    document.getElementById('nightwear-table').style.display = 'block';
    document.getElementById('ladies-frock-table').style.display = 'none';
    document.getElementById('ladies-blouse-table').style.display = 'none';
    document.getElementById('ladies-pant-table').style.display = 'none';
    document.getElementById('ladies-skirt-table').style.display = 'none';
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';

    //sub menu
    document.getElementById('nightwear').style.background = 'grey';
    document.getElementById('ladies-frock').style.background = 'white';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';

    //top
    document.getElementById('nightwear-top').style.display = 'block';
    document.getElementById('ladies-frock-top').style.display = 'none';
    document.getElementById('ladies-blouse-top').style.display = 'none';
    document.getElementById('ladies-pant-top').style.display = 'none';
    document.getElementById('ladies-skirt-top').style.display = 'none';
    document.getElementById('ladies-tshirt-top').style.display = 'none';
    document.getElementById('maternity-frock-top').style.display = 'none';
    document.getElementById('kaftan-top').style.display = 'none';
}

function NightwearDisplayForm() {
    document.getElementById('nightwear-form').style.display = 'block';
}

function NightwearCloseForm() {
    document.getElementById('nightwear-form').style.display = 'none';
}

function BoysPant() {
    //table
    document.getElementById('boys-pant-table').style.display = 'block';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    //submenu
    document.getElementById('boys-pant').style.background = 'grey';
    document.getElementById('boys-shirt').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';

    //top
    document.getElementById('boys-pant-top').style.display = 'block';
    document.getElementById('boys-shirt-top').style.display = 'none';
    document.getElementById('boys-tshirt-top').style.display = 'none';
    document.getElementById('boys-short-top').style.display = 'none';
}

function BoysPantDisplayForm() {
    document.getElementById('boys-pant-form').style.display = 'block';
}

function  BoysPantCloseForm() {
    document.getElementById('boys-pant-form').style.display = 'none';
}

function BoysShirt() {
    //table
    document.getElementById('boys-shirt-table').style.display = 'block';
    document.getElementById('boys-pant-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    //submenu
    document.getElementById('boys-shirt').style.background = 'grey';
    document.getElementById('boys-pant').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';

    // sub
    document.getElementById('boys-shirt-top').style.display = 'block';
    document.getElementById('boys-pant-top').style.display = 'none';
    document.getElementById('boys-tshirt-top').style.display = 'none';
    document.getElementById('boys-short-top').style.display = 'none';
}

function BoysShirtDisplayForm() {
    document.getElementById('boys-shirt-form').style.display = 'block';
}

function  BoysShirtCloseForm() {
    document.getElementById('boys-shirt-form').style.display = 'none';
}

function BoysTshirt() {
    //table
    document.getElementById('boys-tshirt-table').style.display = 'block';
    document.getElementById('boys-pant-table').style.display = 'none';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    //submenu
    document.getElementById('boys-tshirt').style.background = 'grey';
    document.getElementById('boys-pant').style.background = 'white';
    document.getElementById('boys-shirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';

    // sub
    document.getElementById('boys-tshirt-top').style.display = 'block';
    document.getElementById('boys-pant-top').style.display = 'none';
    document.getElementById('boys-shirt-top').style.display = 'none';
    document.getElementById('boys-short-top').style.display = 'none';
}

function BoysTshirtDisplayForm() {
    document.getElementById('boys-tshirt-form').style.display = 'block';
}

function  BoysTshirtCloseForm() {
    document.getElementById('boys-tshirt-form').style.display = 'none';
}

function BoysShort() {
    //table
    document.getElementById('boys-short-table').style.display = 'block';
    document.getElementById('boys-pant-table').style.display = 'none';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';

    //submenu
    document.getElementById('boys-short').style.background = 'grey';
    document.getElementById('boys-pant').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-shirt').style.background = 'white'

    // sub
    document.getElementById('boys-short-top').style.display = 'block';
    document.getElementById('boys-pant-top').style.display = 'none';
    document.getElementById('boys-shirt-top').style.display = 'none';
    document.getElementById('boys-tshirt-top').style.display = 'none';
}

function BoysShortDisplayForm() {
    document.getElementById('boys-short-form').style.display = 'block';
}

function  BoysShortCloseForm() {
    document.getElementById('boys-short-form').style.display = 'none';
}

function GirlsFrock() {
    //table
    document.getElementById('girls-frock-table').style.display = 'block';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    //submenu
    document.getElementById('girls-frock').style.background = 'grey';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-tshirt').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';

    //top
    document.getElementById('girls-frock-top').style.display = 'block';
    document.getElementById('girls-pant-top').style.display = 'none';
    document.getElementById('girls-tshirt-top').style.display = 'none';
    document.getElementById('girls-short-top').style.display = 'none';
}

function GirlsFrockDisplayForm() {
    document.getElementById('girls-frock-form').style.display = 'block';
}

function GirlsFrockCloseForm() {
    document.getElementById('girls-frock-form').style.display = 'none';
}

function GirlsPant() {
    //table
    document.getElementById('girls-pant-table').style.display = 'block';
    document.getElementById('girls-frock-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    //submenu
    document.getElementById('girls-pant').style.background = 'grey';
    document.getElementById('girls-frock').style.background = 'white';
    document.getElementById('girls-tshirt').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';

    //top
    document.getElementById('girls-pant-top').style.display = 'block';
    document.getElementById('girls-frock-top').style.display = 'none';
    document.getElementById('girls-tshirt-top').style.display = 'none';
    document.getElementById('girls-short-top').style.display = 'none';
}

function GirlsPantDisplayForm() {
    document.getElementById('girls-pant-form').style.display = 'block';
}

function GirlsPantCloseForm() {
    document.getElementById('girls-pant-form').style.display = 'none';
}

function GirlsTshirt() {
    //table
    document.getElementById('girls-tshirt-table').style.display = 'block';
    document.getElementById('girls-frock-table').style.display = 'none';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    //submenu
    document.getElementById('girls-tshirt').style.background = 'grey';
    document.getElementById('girls-frock').style.background = 'white';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';

    //top
    document.getElementById('girls-tshirt-top').style.display = 'block';
    document.getElementById('girls-frock-top').style.display = 'none';
    document.getElementById('girls-pant-top').style.display = 'none';
    document.getElementById('girls-short-top').style.display = 'none';
}

function GirlsTshirtDisplayForm() {
    document.getElementById('girls-tshirt-form').style.display = 'block';
}

function GirlsTshirtCloseForm() {
    document.getElementById('girls-tshirt-form').style.display = 'none';
}

function GirlsShort() {
    //table
    document.getElementById('girls-short-table').style.display = 'block';
    document.getElementById('girls-frock-table').style.display = 'none';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';

    //submenu
    document.getElementById('girls-short').style.background = 'grey';
    document.getElementById('girls-frock').style.background = 'white';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-tshirt').style.background = 'white';

    //top
    document.getElementById('girls-short-top').style.display = 'block';
    document.getElementById('girls-frock-top').style.display = 'none';
    document.getElementById('girls-pant-top').style.display = 'none';
    document.getElementById('girls-tshirt-top').style.display = 'none';
}

function GirlsShortDisplayForm() {
    document.getElementById('girls-short-form').style.display = 'block';
}

function GirlsShortCloseForm() {
    document.getElementById('girls-short-form').style.display = 'none';
}

function InfantsFrock() {
    //table
    document.getElementById('infant-frock-table').style.display = 'block';
    document.getElementById('infant-pant-table').style.display = 'none';

    // submenu
    document.getElementById('infants-frock').style.background = 'grey';
    document.getElementById('infants-pant').style.background = 'white';

    // top
    document.getElementById('infants-frock-top').style.display = 'block';
    document.getElementById('infants-pant-top').style.display = 'none';
}

function InfantsFrockDisplayForm() {
    document.getElementById('infants-frock-form').style.display = 'block';
}

function InfantsFrockCloseForm() {
    document.getElementById('infants-frock-form').style.display = 'none';
}

function InfantsPant() {
    //table
    document.getElementById('infant-pant-table').style.display = 'block';
    document.getElementById('infant-frock-table').style.display = 'none';

    // submenu
    document.getElementById('infants-pant').style.background = 'grey';
    document.getElementById('infants-frock').style.background = 'white';

    // top
    document.getElementById('infants-pant-top').style.display = 'block';
    document.getElementById('infants-frock-top').style.display = 'none';
}

function InfantsPantDisplayForm() {
    document.getElementById('infants-pant-form').style.display = 'block';
}

function InfantsPantCloseForm() {
    document.getElementById('infants-pant-form').style.display = 'none';
}

function TeensFrockDisplayForm() {
    document.getElementById('teens-frock-form').style.display = 'block';
}

function TeensFrockCloseForm() {
    document.getElementById('teens-frock-form').style.display = 'none';
}

// Accept/ Reject
function ShowLadiesFrockTable(select) {
    if (select.value === 0){
        document.getElementById('ladies-frock-table').style.display = 'block';
    } else {
         document.getElementById('ladies-frock-table').style.display = 'none';
    }
}