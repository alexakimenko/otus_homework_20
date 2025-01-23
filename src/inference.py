import numpy as np

class StubModelWrapper:
    def __init__(self):
        # Пока нет реальной модели, не грузим ничего
        np.random.seed(42)

    def predict(self, features: np.ndarray):
        """
        Возвращает случайное предсказание в виде массива,
        например, один float в диапазоне [0,1].
        """
        n_samples = features.shape[0]
        return np.random.rand(n_samples)


model_wrapper = StubModelWrapper()

def get_prediction(features: list[float]) -> list[float]:
    """
    Принимает список чисел (признаки),
    Превращает в np.array -> передаёт в model_wrapper.predict
    Возвращает первое предсказание (float).
    """
    X = np.array(features).reshape(1, -1)
    return model_wrapper.predict(X)
