from math import sin, pi
from numpy import array, zeros
from scipy.io.wavfile import write
from time import sleep


class Nota:
    """
    Esta clase puede crear objetos tono que tienen un sonido dentro de la escala musical
    y guardarlos en un archivo con formato .wav

    Sus parámetros son
        @tono: nombre del tono como string
        @fs: (opcional) frecuencia de muestreo. Si no se escribe nada será la estándar 44100
        @inter: (opcional) booleano que indica si se quiere un silencio o espacio después del tono
                si no se escribe nada será False

        Ejemplo:
                re = Nota('re')
    """
    def __init__(self, tono, fs=44100, inter=False):
        self.tono = tono.upper()
        self.fs = fs
        self.inter = inter
        self.tonos = {
            'DO5': 523.25,
            'DO': 261.63,
            'RE': 293.66,
            'MI': 329.63,
            'FA': 349.23,
            'SOL': 392,
            'LA': 440,
            'SI': 493.88
        }

    def _freq_nota(self):
        """
        La función de este método es buscar el tono indicado como string en el constructor
        y retornar la frecuencia que es una de entre los atributos del constructor

        :return: freq_tonos[tono]

        Para agregar un nuevo tono
            1) Define la frecuencia la que debe vibrar
                    Ejemplo:
                        do5 oscila a 523.25 Hz
            2) Insertalo como atributo en el diccionario del constructor. Con su KEY en mayúsculas
        """
        try:
            tono = float(self.tonos[self.tono])
        except KeyError:
            tono = None
            print('Ese tono aún no está disponible o no existe')

        return tono

    def vibrar(self):
        """
        Entrega un array con las muestras a la frecuencia indicada en el constructor

        w = 2 * pi * self._freq_nota() / self.fs
        nota = []
        espacio = [0, 0]
        for n in range(22050):
            muestra = sin(w * n)
            nota.append(muestra)
            if self.inter is True:
                espacio = list(zeros(3000))
        notas = nota + espacio

        :return: numpy.array(notas)
        """
        w = 2 * pi * self._freq_nota() / self.fs
        nota = []
        espacio = [0, 0]
        for n in range(22050):
            muestra = sin(w * n)
            nota.append(muestra)
            if self.inter is True:
                espacio = list(zeros(3000))
        notas = nota + espacio

        return array(notas)

    def grabar_tono(self):
        """
        Este método sin parámetros llama a la funcion self.vibrar() y luego usando el array que retorna, guarda
        el tono en un archivo wave (.wav) en directorio actal
        :return:
        """
        if self._freq_nota() is None:
            print('La configuración actual no permite ejecutar este método')
        else:
            print('Espera unos segundos')
            nombre = self.tono + '.wav'
            write(nombre, 44100, self.vibrar())
            sleep(3)
            print('Tono listo ' + nombre + '. En el directorio actual')

