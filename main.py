from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__,template_folder='templates')

# Conecta ao banco de dados
def connect_db():
    return sqlite3.connect('tasks.db')

# Exibe a lista de tarefas
@app.route('/')
def show_tasks():
    # Conecta ao banco de dados
    conn = connect_db()
    c = conn.cursor()

    # Seleciona todas as tarefas pendentes do banco de dados
    c.execute("SELECT * FROM tasks WHERE status='pending'")
    tasks = c.fetchall()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Renderiza a página HTML com a lista de tarefas
    return render_template('show_tasks.html', tasks=tasks)

# Adiciona uma nova tarefa
@app.route('/add_task', methods=['POST'])
def add_task():
    # Obtém os dados do formulário
    task_name = request.form['task_name']

    # Conecta ao banco de dados
    conn = connect_db()
    c = conn.cursor()

    # Insere a nova tarefa no banco de dados
    c.execute("INSERT INTO tasks (task_name, status) VALUES (?, 'pending')", (task_name,))

    # Salva as alterações no banco de dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Redireciona o usuário para a página principal
    return redirect(url_for('show_tasks'))

# Marca uma tarefa como concluída
@app.route('/complete_task/<task_id>')
def complete_task(task_id):
    # Conecta ao banco de dados
    conn = connect_db()
    c = conn.cursor()

    # Atualiza o status da tarefa para "concluída" no banco de dados
    c.execute("UPDATE tasks SET status='completed' WHERE task_id=?", (task_id,))

    # Salva as alterações no banco de dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Redireciona o usuário para a página principal
    return redirect(url_for('show_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
