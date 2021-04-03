function inputMask(selector, masked) {
//    Выбор необходимого input при помощи селектора (id)
    const element = document.querySelectorAll(selector);

    // Маска со страндартными проверками для любого input
    function mask(event) {

        // Хранит код нажатой клавиши (необходима для валидации)
        const keyCode = event.keyCode
        // Копирует маску в константу
        const template = masked;
        // def - хранит цифры находящиеся в шаблоне, удаляя все остальное
        const def = template.replace(/\D/g, "");
        // val - сохраняет цифры, которые ввел пользователь, игнорируя все остальное
        const val = this.value.replace(/\D/g, "");
        // Счетчик
        let i = 0
        // Значение которое вносится в input
        let newValue = template.replace(/[_\d]/g, function (a) {
            // Если счетчик меньше длины номера, то сначала возвращается код региона,
            // а затем введенные пользователем цифры, после возвращается нижнее подчеркивание
            if (i < val.length) {
                return val.charAt(i++) || def.charAt(i);
            } else {
                return a;
            }
        })
        // Обновление счетчика (принимает значение первого найденного "_")
        i = newValue.indexOf("_")

        // newValue принимает значение без "_"
        if (i !== -1) {
            newValue = newValue.slice(0, i);
        }

        // reg - шаблон регулярного выражения
        // Возвращает часть шаблона начиная с 0 и заканчивая длиной input
        let reg = template.substr(0, this.value.length);

        // Собирает шаблон регулярного выражения
        reg = reg.replace(/_+/g, function (a) {
            return `\\d{1,${a.length}}`;
        });

        // Дополняет шаблон перед знаками "+()"
        reg = reg.replace(/[+()]/g, "\\$&");

        // Создание регулярного выражения
		reg = new RegExp(`^${reg}$`);


		// Проверка элемента формы "Снилс"
		if (selector === "#snils") {
            if (!reg.test(this.value) || keyCode > 47 && keyCode < 58) {
			    this.value = newValue;
		    }
        }

	    // Проверка элемента формы "Номер телефона"
        if (selector === "#phone_number") {
            if (!reg.test(this.value) || this.value.length < 5 || keyCode > 47 && keyCode < 58) {
			    this.value = newValue;
		    }
		    if (event.type === "blur" && this.value.length < 5) {
			    this.value = "";
		    }
        }
    }

    // Добавление обработчиков событий
    for (const elem of element) {
        elem.addEventListener("input", mask);
        elem.addEventListener("focus", mask);
        elem.addEventListener("blur", mask);
    }
}

inputMask("#phone_number", "+7 (___)-___-__-__");
inputMask("#snils", "___-___-___-__");