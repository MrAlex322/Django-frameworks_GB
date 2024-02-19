from django.shortcuts import render
import logging

# Получаем экземпляр объекта логгера для данного приложения
logger = logging.getLogger(__name__)


def home(request):
    # Логика для определения контекста
    context = {
        'title': 'Добро пожаловать на мой сайт!',
        'content': 'Здесь вы найдете много интересного о моем первом Django-приложении.'
    }

    # Логируем посещение главной страницы
    logger.info('Пользователь посетил главную страницу')

    return render(request, 'proj/home.html', context)


def about(request):
    # Логика для определения контекста
    context = {
        'title': 'Обо мне',
        'content': 'Привет! Меня зовут Александр, и я создатель этого сайта. Я очень рад приветствовать вас здесь.'
    }

    # Логируем посещение страницы "о себе"
    logger.info('Пользователь посетил страницу "О себе"')

    return render(request, 'proj/about.html', context)
