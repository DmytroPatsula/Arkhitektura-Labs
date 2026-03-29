import threading
import time

variants_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lock = threading.Lock()

def take_variant(student_name):
    global variants_pool

    with lock:
        if len(variants_pool) > 0:

            my_variant = variants_pool.pop(0)
            print(f"{student_name} отримав варіант №{my_variant}")
        else:
            print(f"{student_name} залишився без варіанту (завдання закінчились)")
    time.sleep(0.5)

def main():
    threads = []
    for i in range(1, 13):
        t = threading.Thread(target=take_variant, args=(f"Студент {i}",))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
    print("\nРозподіл завершено!")
    print(f"Залишок варіантів у пулі: {variants_pool}")

if __name__ == "__main__":
    main()