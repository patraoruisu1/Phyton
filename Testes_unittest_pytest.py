import unittest
from unittest.mock import patch, MagicMock

# Classe para testar
class EmailService:
    def __init__(self, smtp_server):
        self.smtp_server = smtp_server
    
    def send_email(self, to, subject, body):
        if '@' not in to:
            raise ValueError("Email inválido")
        
        # Simula envio de email
        return f"Email enviado para {to}"

# Testes com unittest
class TestEmailService(unittest.TestCase):
    def setUp(self):
        self.email_service = EmailService("smtp.example.com")
    
    def test_send_valid_email(self):
        result = self.email_service.send_email(
            "test@example.com", 
            "Teste", 
            "Corpo do email"
        )
        self.assertEqual(result, "Email enviado para test@example.com")
    
    def test_send_invalid_email(self):
        with self.assertRaises(ValueError):
            self.email_service.send_email("email-inválido", "Teste", "Corpo")
    
    @patch('requests.post')
    def test_api_call(self, mock_post):
        # Mock de chamada HTTP
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'status': 'success'}
        
        # Teste com mock
        # ... código que faz chamada HTTP

# Versão pytest (mais simples)
def test_email_valid():
    service = EmailService("smtp.test.com")
    result = service.send_email("test@example.com", "Teste", "Corpo")
    assert result == "Email enviado para test@example.com"

def test_email_invalid():
    service = EmailService("smtp.test.com")
    with pytest.raises(ValueError):
        service.send_email("email-inválido", "Teste", "Corpo")