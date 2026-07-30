<?php
declare(strict_types=1);

namespace App\Repositories\Product;

use App\Models\Product;

class ProductRepository implements ProductRepositoryInterface
{
    public function __construct(private Product $model) {}

    public function getAll(): array
    {
        return $this->model->all()->toArray();
    }

    public function findById(int $id): array
    {
        return $this->model->findOrFail($id)->toArray();
    }

    public function create(array $data): array
    {
        return $this->model->create($data)->toArray();
    }

    public function update(int $id, array $data): array
    {
        $record = $this->model->findOrFail($id);
        $record->update($data);

        return $record->toArray();
    }

    public function delete(int $id): void
    {
        $this->model->findOrFail($id)->delete();
    }
}