import threading
import time

# Intervalo de batimentos cardíacos (em segundos)
HEARTBEAT_INTERVAL = 2
# Limite de detecção de falhas (em segundos)
DETECTION_THRESHOLD = 5
# Número de heartbeats antes de forçar uma falha
FORCE_FAILURE_AFTER = 5

class HeartbeatDetector:
    def __init__(self):
        # Evento para indicar se um heartbeat foi recebido
        self.heartbeat_event = threading.Event()
        # Controle de execução dos loops
        self.running = True
        # Contador de heartbeats enviados
        self.heartbeat_count = 0

    def start(self):
        # Inicia o envio de heartbeats
        self.start_heartbeat()
        # Inicia a detecção de falhas
        self.start_detection()

    def start_heartbeat(self):
        def send_heartbeat():
            # Continua enviando heartbeats enquanto o detector estiver em execução
            while self.running:
                time.sleep(HEARTBEAT_INTERVAL)
                self.send_heartbeat()

        # Cria e inicia uma thread para enviar heartbeats
        heartbeat_thread = threading.Thread(target=send_heartbeat)
        heartbeat_thread.daemon = True
        heartbeat_thread.start()

    def send_heartbeat(self):
        if self.heartbeat_count < FORCE_FAILURE_AFTER:
            # Simulação do envio de um heartbeat
            print("Enviando heartbeat...")
            # Define o evento indicando que um heartbeat foi enviado
            self.heartbeat_event.set()
            # Incrementa o contador de heartbeats enviados
            self.heartbeat_count += 1
        else:
            # Simulação de falha ao não enviar um heartbeat
            print("Erro forçado: heartbeat não enviado.")
            self.heartbeat_event.clear()

    def start_detection(self):
        while self.running:
            time.sleep(DETECTION_THRESHOLD)
            self.check_heartbeat()

    def check_heartbeat(self):
        if self.heartbeat_event.is_set():
            # Se um heartbeat foi recebido, o sistema está saudável
            print("Heartbeat recebido. Sistema está saudável.")
            # Limpa o evento para a próxima verificação
            self.heartbeat_event.clear()
        else:
            # Se um heartbeat não foi recebido, uma falha é detectada
            print("Falha detectada! Heartbeat não recebido.")
            self.handle_failure()

    def handle_failure(self):
        # Lógica de tratamento de falha
        print("Executando procedimentos de recuperação...")
        # Para a execução dos loops
        self.running = False

if __name__ == "__main__":
    detector = HeartbeatDetector()
    detector.start()

    # Simulação de execução do sistema
    try:
        while detector.running:
            time.sleep(1)
    except KeyboardInterrupt:
        # Interrompe a execução ao receber um sinal de interrupção (Ctrl+C)
        detector.running = False
