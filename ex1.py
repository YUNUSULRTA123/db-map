import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def ax_cr(file="stock_w.png"):
    # Создаем новый график с указанной проекцией Mollweide
    ax = plt.axes(projection=ccrs.Mollweide())

    # Добавляем стандартное изображение карты мира на график
    ax.stock_img()
    plt.savefig(file, dpi=300)
    plt.close()
    return file

if __name__ == "__main__":
    file_name = ax_cr()
    print(f"График для всех классов сохранён в файл: {file_name}")