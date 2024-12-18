from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def lab9_name():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('lab9.lab9_age', username=username))
    return render_template('lab9/lab9_name.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def lab9_age():
    username = request.args.get('username')
    if request.method == 'POST':
        age = request.form['age']
        return redirect(url_for('lab9.lab9_gender', username=username, age=age))
    return render_template('lab9/lab9_age.html', username=username)

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def lab9_gender():
    username = request.args.get('username')
    age = request.args.get('age')
    if request.method == 'POST':
        gender = request.form['gender']
        return redirect(url_for('lab9.lab9_question', username=username, age=age, gender=gender))
    return render_template('lab9/lab9_sex.html', username=username, age=age)

@lab9.route('/lab9/question', methods=['GET', 'POST'])
def lab9_question():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')

    if request.method == 'POST':
        answer = request.form['answer']
        return redirect(url_for('lab9.lab9_question2', username=username, age=age, gender=gender, answer=answer))

    return render_template('lab9/lab9_question.html', username=username, age=age, gender=gender)

@lab9.route('/lab9/question2', methods=['GET', 'POST'])
def lab9_question2():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    answer = request.args.get('answer')

    if answer == "Паста":
        question = "Какую пасту выберете?"
        option1 = "Карбонара"
        option2 = "Болоньезе"
    elif answer == "Пицца":
        question = "Какую пиццу выберете?"
        option1 = "Маргарита"
        option2 = "Четыре сыра"

    if request.method == 'POST':
        second_answer = request.form['answer']
        
        if answer == "Паста":  
            if second_answer == 'Карбонара':
                if int(age) < 18:  
                    congratulation = f"Дорогой {username}, с наступающим Новым годом! Пусть в новом году ты наслаждаешься моментами, как пастой Карбонара. Пусть твоя жизнь будет такой же насыщенной и вкусной, как эта паста! Пусть сбудется все, о чем ты мечтаешь!"
                    image = "karb.png"  
                else: 
                    congratulation = f"С наступающим Новым годом, {username}! Пусть в новом году каждый день будет таким же вкусным и насыщенным, как паста Карбонара. Пусть твоя жизнь будет полной успехов и радостных моментов!"
                    image = "karb.png"  
            elif second_answer == 'Болоньезе':
                if int(age) < 18:  
                    congratulation = f"Дорогой {username}, с наступающим Новым годом! Пусть каждый день будет таким же вкусным и ярким, как паста Болоньезе! Желаю тебе счастья, радости и много сладких моментов в новом году!"
                    image = "bol.webp"  
                else:  
                    congratulation = f"С наступающим Новым годом, {username}! Пусть в новом году твоя жизнь будет такой же насыщенной, как паста Болоньезе. Пусть каждый день будет полон радости, удачи и новых свершений!"
                    image = "bol.webp"  
        elif answer == "Пицца":
            if second_answer == 'Маргарита':
                if int(age) < 18: 
                    congratulation = f"Дорогой {username}, с наступающим Новым годом! Пусть твоя жизнь будет такой же яркой и вкусной, как пицца Маргарита! Пусть в новом году сбудется все, о чем ты мечтаешь!"
                    image = "margo.webp"
                else: 
                    congratulation = f"С наступающим Новым годом, {username}! Пусть в новом году твоя жизнь будет такой же насыщенной и яркой, как пицца Маргарита. Пусть успех и радость всегда сопровождают тебя!"
                    image = "margo.webp" 
            elif second_answer == 'Четыре сыра':
                if int(age) < 18:  
                    congratulation = f"Дорогой {username}, с наступающим Новым годом! Пусть новый год принесет тебе столько радости, сколько разных сыров на пицце с четырьмя сырами! Желаю тебе много сладких и ярких моментов!"
                    image = "cheese.png"
                else:  
                    congratulation = f"С наступающим Новым годом, {username}! Пусть новый год принесет тебе столько счастья, сколько разных сыров в пицце с четырьмя сырами. Пусть жизнь будет насыщенной и успешной!"
                    image = "cheese.png"

        return render_template('lab9/lab9_final.html', congratulation=congratulation, image=image, username=username, age=age, gender=gender)

    return render_template('lab9/lab9_question2.html', username=username, age=age, gender=gender, question=question, option1=option1, option2=option2)
