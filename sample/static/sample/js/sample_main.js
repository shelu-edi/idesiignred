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

    // Wrappers
    document.getElementById('boys-tables-wrapper').style.display = 'block';
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
    document.getElementById('girls-table-wrapper').style.display = 'none';
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

    // Wrappers
    document.getElementById('girls-table-wrapper').style.display = 'block';
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
    document.getElementById('boys-tables-wrapper').style.display = 'none';
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

    // Wrappers
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
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

    // Wrappers
    document.getElementById('ladies-tables-wrapper').style.display = 'none';
}

function LadiesFrock() {
    //tables
    document.getElementById('ladies-frock-table').style.display = 'inline-table';
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
}

function LadiesBlouse() {
    //table
    document.getElementById('ladies-blouse-table').style.display = 'inline-table';
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
}

function LadiesPant() {
    //table
    document.getElementById('ladies-pant-table').style.display = 'inline-table';
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
}

function LadiesSkirt() {
    //table
    document.getElementById('ladies-skirt-table').style.display = 'inline-table';
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
}

function LadiesTshirt() {
    //table
    document.getElementById('ladies-tshirt-table').style.display = 'inline-table';
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
}

function MaternityFrock() {
    //table
    document.getElementById('maternity-frock-table').style.display = 'inline-table';
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
}

function Kaftan() {
    //table
    document.getElementById('kaftan-table').style.display = 'inline-table';
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
}

function Nightwear() {
    //table
    document.getElementById('nightwear-table').style.display = 'inline-table';
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
}

function BoysPant() {
    //table
    document.getElementById('boys-pant-table').style.display = 'inline-table';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    //submenu
    document.getElementById('boys-pant').style.background = 'grey';
    document.getElementById('boys-shirt').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';
}

function BoysShirt() {
    //table
    document.getElementById('boys-shirt-table').style.display = 'inline-table';
    document.getElementById('boys-pant-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    //submenu
    document.getElementById('boys-shirt').style.background = 'grey';
    document.getElementById('boys-pant').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';
}

function BoysTshirt() {
    //table
    document.getElementById('boys-tshirt-table').style.display = 'inline-table';
    document.getElementById('boys-pant-table').style.display = 'none';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-short-table').style.display = 'none';

    //submenu
    document.getElementById('boys-tshirt').style.background = 'grey';
    document.getElementById('boys-pant').style.background = 'white';
    document.getElementById('boys-shirt').style.background = 'white';
    document.getElementById('boys-short').style.background = 'white';
}

function BoysShort() {
    //table
    document.getElementById('boys-short-table').style.display = 'inline-table';
    document.getElementById('boys-pant-table').style.display = 'none';
    document.getElementById('boys-shirt-table').style.display = 'none';
    document.getElementById('boys-tshirt-table').style.display = 'none';

    //submenu
    document.getElementById('boys-short').style.background = 'grey';
    document.getElementById('boys-pant').style.background = 'white';
    document.getElementById('boys-tshirt').style.background = 'white';
    document.getElementById('boys-shirt').style.background = 'white';
}

function GirlsFrock() {
    //table
    document.getElementById('girls-frock-table').style.display = 'inline-table';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    //submenu
    document.getElementById('girls-frock').style.background = 'grey';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-tshirt').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';
}

function GirlsPant() {
    //table
    document.getElementById('girls-pant-table').style.display = 'inline-table';
    document.getElementById('girls-frock-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    //submenu
    document.getElementById('girls-pant').style.background = 'grey';
    document.getElementById('girls-frock').style.background = 'white';
    document.getElementById('girls-tshirt').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';

}

function GirlsTshirt() {
    //table
    document.getElementById('girls-tshirt-table').style.display = 'inline-table';
    document.getElementById('girls-frock-table').style.display = 'none';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-short-table').style.display = 'none';

    //submenu
    document.getElementById('girls-tshirt').style.background = 'grey';
    document.getElementById('girls-frock').style.background = 'white';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-short').style.background = 'white';

}

function GirlsShort() {
    //table
    document.getElementById('girls-short-table').style.display = 'inline-table';
    document.getElementById('girls-frock-table').style.display = 'none';
    document.getElementById('girls-pant-table').style.display = 'none';
    document.getElementById('girls-tshirt-table').style.display = 'none';

    //submenu
    document.getElementById('girls-short').style.background = 'grey';
    document.getElementById('girls-frock').style.background = 'white';
    document.getElementById('girls-pant').style.background = 'white';
    document.getElementById('girls-short').style.background = 'grey';

}