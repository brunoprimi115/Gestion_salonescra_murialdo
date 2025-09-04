from datetime import time
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Horario permitido
HORA_APERTURA = time(8, 0)   # 08:00
HORA_CIERRE = time(18, 0)    # 18:00

def validar_horario_reserva(inicio, fin):
    """
    Valida que la reserva esté dentro del horario permitido (08:00 - 18:00).
    """
    if inicio.time() < HORA_APERTURA or fin.time() > HORA_CIERRE:
        raise ValidationError(
            _(f"Las reservas solo están permitidas entre {HORA_APERTURA.strftime('%H:%M')} y {HORA_CIERRE.strftime('%H:%M')}.")
        )

    if inicio >= fin:
        raise ValidationError(_("La hora de fin debe ser mayor que la hora de inicio."))
