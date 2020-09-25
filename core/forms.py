from django import forms
from django.core.mail import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):  # Esse não vai pro banco de dados
  nome = forms.CharField(label='Nome', max_length=100)
  email = forms.EmailField(label='E-mail', max_length=120)
  assunto = forms.CharField(label='Assunto', max_length=120)
  mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

  def send_mail(self):
    nome = self.cleaned_data['nome']
    email = self.cleaned_data['email']
    assunto = self.cleaned_data['assunto']
    mensagem = self.cleaned_data['mensagem']

    conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

    mail = EmailMessage(
      subject='E-mail enviado pelo sistema Django2',
      body=conteudo,
      from_email='contato@seudominio.com.br',
      to=['contato@seudominio.com.br', 'outro@seudominio.com.br'],
      headers={'Reply-To': email}
    )

    mail.send()


class ProdutoModelForm(forms.ModelForm):  # Esse vai pro banco de dados, por isso o model
  class Meta:
    model = Produto
    fields = ['nome', 'preco', 'estoque', 'imagem']

