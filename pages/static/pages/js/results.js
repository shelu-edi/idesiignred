function EmptyTable(MyClass) {
    let tds = document.getElementsByClassName(MyClass);
    let hide = false

    for (let element of tds) {
      if (element.innerHTML.length == 0) hide = true
    }
    let myTable = document.getElementById(MyClass);
    if (hide)myTable.style.display = 'none';
}

EmptyTable('customer__wrapper')