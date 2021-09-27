console.log('blah')

function LadiesSub() {

    // Sub Categories
    document.getElementById('ladies-sub').style.display = 'flex';
    document.getElementById('boys-sub').style.display = 'none';
    document.getElementById('girls-sub').style.display = 'none';
    document.getElementById('infants-sub').style.display = 'none';
    document.getElementById('teens-sub').style.display = 'none';

    // Main Categories
    document.getElementById('ladies-main').style.background = 'grey';
    document.getElementById('boys-main').style.background = 'white';
    document.getElementById('girls-main').style.background = 'white';
    document.getElementById('infants-main').style.background = 'white';
    document.getElementById('teens-main').style.background = 'white';

    // Wrappers
    document.getElementById('ladies-tables-wrapper').style.display = 'block';
    document.getElementById('boys-tables-wrapper').style.display = 'none';
    document.getElementById('girls-table-wrapper').style.display = 'none';
    document.getElementById('infant-table-wrapper').style.display = 'none';
    document.getElementById('teens-tables-wrapper').style.display = 'none';
}

function BoysSub() {
    // Sub Categories
    document.getElementById('boys-sub').style.display = 'flex';
    document.getElementById('ladies-sub').style.display = 'none';
    document.getElementById('girls-sub').style.display = 'none';
    document.getElementById('infants-sub').style.display = 'none';
    document.getElementById('teens-sub').style.display = 'none';

    // Main Categories
    document.getElementById('boys-main').style.background = 'grey';
    document.getElementById('ladies-main').style.background = 'white';
    document.getElementById('girls-main').style.background = 'white';
    document.getElementById('infants-main').style.background = 'white';
    document.getElementById('teens-main').style.background = 'white';

    //boys sub
    document.getElementById('boys-pant').style.background = 'grey';
    document.getElementById('boys-shirt').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';

    // boys tables
    document.getElementById('boys-pant-table').style.display = 'block';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    // Wrappers
    document.getElementById('boys-tables-wrapper').style.display = 'block';
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
    document.getElementById('girls-table-wrapper').style.display = 'none';
    document.getElementById('infant-table-wrapper').style.display = 'none';
    document.getElementById('teens-tables-wrapper').style.display = 'none';

    //top
    document.getElementById('boys-pant-top').style.display = 'block';
}

function GirlsSub() {
    // Sub Categories
    document.getElementById('girls-sub').style.display = 'flex';
    document.getElementById('ladies-sub').style.display = 'none';
    document.getElementById('boys-sub').style.display = 'none';
    document.getElementById('infants-sub').style.display = 'none';
    document.getElementById('teens-sub').style.display = 'none';

    // Main Categories
    document.getElementById('girls-main').style.background = 'grey';
    document.getElementById('ladies-main').style.background = 'white';
    document.getElementById('boys-main').style.background = 'white';
    document.getElementById('infants-main').style.background = 'white';
    document.getElementById('teens-main').style.background = 'white';

    // Girls Sub
    document.getElementById('girls-frock').style.background = 'grey';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-tshirt').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';

    // Girls Table
    document.getElementById('girls-frock-table').style.display = 'block';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    // Wrappers
    document.getElementById('girls-table-wrapper').style.display = 'block';
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
    document.getElementById('boys-tables-wrapper').style.display = 'none';
    document.getElementById('infant-table-wrapper').style.display = 'none';
    document.getElementById('teens-tables-wrapper').style.display = 'none';

    //top
    document.getElementById('girls-frock-top').style.display = 'block';
}

function InfantsSub() {
    // Sub Categories
    document.getElementById('infants-sub').style.display = 'flex';
    document.getElementById('ladies-sub').style.display = 'none';
    document.getElementById('boys-sub').style.display = 'none';
    document.getElementById('girls-sub').style.display = 'none';
    document.getElementById('teens-sub').style.display = 'none';

    // Main Categories
    document.getElementById('infants-main').style.background = 'grey';
    document.getElementById('ladies-main').style.background = 'white';
    document.getElementById('boys-main').style.background = 'white';
    document.getElementById('girls-main').style.background = 'white';
    document.getElementById('teens-main').style.background = 'white';

    // Infant Sub
    document.getElementById('infants-frock').style.background = 'grey';
    document.getElementById('infants-pant').style.background = 'white';

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
}

function TeensSub() {
    // Sub Categories
    document.getElementById('teens-sub').style.display = 'flex';
    document.getElementById('ladies-sub').style.display = 'none';
    document.getElementById('boys-sub').style.display = 'none';
    document.getElementById('girls-sub').style.display = 'none';
    document.getElementById('infants-sub').style.display = 'none';

    // Main Categories
    document.getElementById('teens-main').style.background = 'grey';
    document.getElementById('ladies-main').style.background = 'white';
    document.getElementById('boys-main').style.background = 'white';
    document.getElementById('girls-main').style.background = 'white';
    document.getElementById('infants-main').style.background = 'white';

    // Teens Sub
    document.getElementById('teens-frock').style.background = 'grey';

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
    document.getElementById('ladies-tshirt-table').style.display = 'none';
    document.getElementById('maternity-frock-table').style.display = 'none';
    document.getElementById('kaftan-table').style.display = 'none';
    document.getElementById('nightwear-table').style.display = 'none';

    //sub menu
    document.getElementById('ladies-frock').style.background = 'grey';
    document.getElementById('ladies-blouse').style.background = 'white';
    document.getElementById('ladies-pant').style.background = 'white';
    document.getElementById('ladies-skirt').style.background = 'white';
    document.getElementById('ladies-tshirt').style.background = 'white';
    document.getElementById('maternity-frock').style.background = 'white';
    document.getElementById('kaftan').style.background = 'white';
    document.getElementById('nightwear').style.background = 'white';

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
    if (select.value == 0){
        document.getElementById('ladies-frock-table').style.display = 'block';
    } else {
         document.getElementById('ladies-frock-table').style.display = 'none';
    }
}