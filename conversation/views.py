from django.shortcuts import render, get_object_or_404, redirect
from merchandises.models import Merchandise
from .forms import ConversationMessageForm
from .models import Conversation


def new_conversation(request, merchandise_pk):
    merchandise = get_object_or_404(Merchandise, pk=merchandise_pk)

    if merchandises.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(merchandise=merchandise).filter(members__in=[request.user.id])

    if conversations:
        pass # redirect to conversation
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(merchandise=merchandise)
            conversation.members.add(request.user)
            conversation.members.add(merchandise.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('merchandise:detail', pk=merchandise_pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form':form
    }) 

